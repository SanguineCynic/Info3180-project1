from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
import os, psycopg2
from werkzeug.utils import secure_filename
from app.models import PropertyListing
from .forms import PropertyForm

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Jonathan Astwood")

@app.route('/properties/create', methods=['GET','POST'])
def createproperty():
    formObj = PropertyForm()

    if request.method=='GET':
        return render_template('create.html', form=formObj)
    elif request.method=='POST':
        if formObj.validate_on_submit():
            #HANDLE FORM 
            res = request.form

            #HANDLE IMAGE DATA
            image_file = formObj.photo.data
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)

            #HANDLE FORM INPUTS
            conn = psycopg2.connect(
                host="localhost",
                database="PropertiesDB",
                user=os.environ.get('DATABASE_USERNAME', 'postgres'),
                password= os.environ.get('DATABASE_PASSWORD')
            )
            cur = conn.cursor()

            listing_data = {
                'title': res['title'],
                'num_bedrooms' : res['num_bedrooms'],
                'num_bathrooms' : res['num_bathrooms'],
                'location': res['location'],
                'price' : res['price'],
                'type' : res['type'],
                'description' : res['description'],
                'image_url' : image_path
            }
            
            cur.execute("""
                INSERT INTO listings (title, num_bedrooms, num_bathrooms, location, type, price, description, image_url)
                VALUES (%(title)s, %(num_bedrooms)s, %(num_bedrooms)s, %(location)s, %(type)s, %(price)s, %(description)s, %(image_url)s);
            """, listing_data)

            conn.commit()
            cur.close()
            conn.close()

            

            #END PROCESS
            flash('Property Uploaded', 'success')
            return redirect(url_for('list_properties'))

    return render_template('create.html', form=formObj)

@app.route('/properties/<uploaddir>/<filename>')
def get_property(uploaddir,filename):
    uploads_dir = app.config['UPLOAD_FOLDER']
    return send_from_directory(os.path.join(os.getcwd(),uploads_dir), filename)


@app.route('/properties/')
def list_properties():
    uploads_dir = app.config['UPLOAD_FOLDER']
    properties = get_properties()

    listings = PropertyListing.query.all()
    # print(myDBQuery)
    return render_template('listings.html', properties=listings)

@app.route('/properties/<propertyid>')
def viewproperty(propertyid):
    listing = PropertyListing.query.filter_by(listingid = propertyid)
    return render_template('viewproperty.html', listing = listing[0])

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

#HELPER FUNCTIONS
def get_properties():
    uploadDir = app.config['UPLOAD_FOLDER']
    lst = []
    for root, dirs, files in os.walk(uploadDir):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png', '.jfif', '.webp')):
                lst.append(os.path.join(root, file))
    return lst