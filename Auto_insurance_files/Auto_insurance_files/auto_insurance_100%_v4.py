import streamlit as st  # Streamlit Framework for building interactive Chat Bots.
import time  # time-related functions like delays and timestamps.
import base64  # Encodes/decodes data in Base64 format.
from datetime import datetime  # Handles date and time operations.
import plotly.graph_objects as go  # Creates interactive plots and visualizations.
from PIL import Image  # Handles image processing tasks.
import logging  # Tracks and logs application activity.
import fitz  # PyMuPDF library for working with PDFs.
import io  # Handles in-memory binary streams for data.
from fpdf import FPDF  # Generates PDF documents programmatically.
import re  # Provides regular expressions for pattern matching.
from datetime import date  # Handles date operations.



# Initialize session state variables with default values
if "name_shown" not in st.session_state:
    st.session_state.name_shown = False
if "message_shown" not in st.session_state:
    st.session_state.message_shown = False
if "file_name" not in st.session_state:
    st.session_state["file_name"] = None
if "image_vehicle" not in st.session_state:
    st.session_state["image_vehicle"] = None
if "pdf_file" not in st.session_state:  
    st.session_state.pdf_file = None
if "image_file" not in st.session_state:  
    st.session_state.image_file = None
if "license_uploaded" not in st.session_state:
    st.session_state.license_uploaded = False
if "image_uploaded" not in st.session_state:
    st.session_state.image_uploaded = False
if "show_progress_bar" not in st.session_state:
    st.session_state.show_progress_bar = False
if "expander_open" not in st.session_state:
    st.session_state.expander_open = False
if 'email_error' not in st.session_state:
    st.session_state.email_error = ""
if 'quotation_shown' not in st.session_state:
    st.session_state.quotation_shown = False
if "text_shown" not in st.session_state:
    st.session_state.text_shown = False
if "progress" not in st.session_state:
    st.session_state.progress = 0
if "quotation_id" not in st.session_state:  
    st.session_state.quotation_id = None
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}


#########
#Streamlit functions for displaying pagination, converting into base64, converting utf-8 starts
#########
st.set_page_config(page_title="BotDnA",                   
                   page_icon=":robot_face:",
                   layout="centered",
                   initial_sidebar_state="expanded"
                   )


def img_to_base64(image_path):
    """Convert image to base64."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        logging.error(f"Error converting image to base64: {str(e)}")
        return None

def get_base64_image(image_path):
    """Convert image to utf-8."""
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")
    return base64_image


# material arrow icon
st.markdown(
    """
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    """,
    unsafe_allow_html=True,
)

#########
#Streamlit functions for displaying pagination, botDNA logo, converting utf-8 Ends
#########

# SIDEBAR START - Load and display sidebar image using CSS
st.markdown(
        """
        <style>
        .cover-glow {
            width: 100%;
            height: auto;
            padding: 3px;
            box-shadow: 
                0 0 5px #330000,
                0 0 10px #660000,
                0 0 15px #990000,
                0 0 20px #CC0000,
                0 0 25px #FF0000,
                0 0 30px #FF3333,
                0 0 35px #FF6666;
            position: relative;
            z-index: -1;
            border-radius: 45px;
        }
        .st-emotion-cache-128upt6 {
            position: relative;
            bottom: 0px;
            width: 10%;
            min-width: 10%;
            background-color: #cce7ff;
            display: flex;
            flex-direction: column;
            -webkit-box-align: center;
            align-items: center;
        }
        @media (min-width: 576px) {
            .st-emotion-cache-arzcut {
                padding-left: -16rem;
                padding-right: 60rem;
                background-color: #cce7ff;
            }
        }
        
        .st-emotion-cache-128upt6 {
            display:None;
        }
        
        </style>
        """,
        unsafe_allow_html=True,
    )
img_path = "botdna_logo-05.png"
img_base64 = img_to_base64(img_path)
if img_base64:
    st.sidebar.markdown(
        f'<img src="data:image/png;base64,{img_base64}">',
        unsafe_allow_html=True,
    )
st.sidebar.write('')
st.sidebar.write('')    
st.sidebar.header(':blue[Select the options below]')
nav = st.sidebar.radio('',[':blue[Auto Quote]',':blue[Claims Processing]',':blue[Policy Customization]', ':blue[Underwriting]'])
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')

expander = st.sidebar.popover('Help')
expander.write("botdna.ai (https://botdna.ai),\n\n botdna@ipath.io")
# SIDEBAR END

#To hide the 3 dots css starts
st.markdown(
    """
    <style>
    .stTabs {
            margin-top:-30px;
            margin-left:-255px;
        }
    .st-emotion-cache-12fmjuu {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#To hide the 3 dots Ends 

# text box width css starts
st.markdown("""
                <style>
                div[data-baseweb="input"],div[data-baseweb="select"]  {
                    max-width: 300px;
                }
                </style>
            """, unsafe_allow_html=True)

# text box width css ends

# Background auto insurance image code starts
image_name = "auto_insurance_bg.jpg"  # The local image file

# Convert the image to base64
img_base64 = img_to_base64(image_name)

# If the image was successfully encoded, set it as the background
if img_base64:
    background_css = f"""
    <style>
    html, body, #root, .stApp {{
        height: 100%;
        margin: 0;
    }}
    .stApp {{
        background-image: url('data:image/jpg;base64,{img_base64}');
        background-size: contain;
        background-position: right -5px center;
        background-attachment: fixed;
        display: flex;
        flex-direction: column;
        background-repeat: no-repeat;
        background-color: #cce7ff;
    }}
    body {{
        color: white;
    }}
    .streamlit-expanderHeader {{
        font-size: 20px;
        color: white;
    }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)
# Background auto insurance image code Ends

# Calling css file starts
with open('auto_insurance_100%_v4.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Calling css file ends


# Initializing the first bot message starts
if 'messages' not in st.session_state:
    current_time = datetime.now().strftime('%I:%M:%S %p')
    st.session_state.messages = [
        {"role": "bot", "content": "Hi, I'm here to help you with your Auto insurance quote", 'time': current_time}
    ]
    st.session_state.step = 'initial'
if "messages" not in st.session_state:
    current_time = datetime.now().strftime('%I:%M:%S %p')
    st.session_state.messages = [{"role": "bot", "content": "Hi, I'm here to help you with your Auto insurance quote", 'time': current_time}]
# Initializing the first bot message ends

######
# virtual assistant functions coding starts
######
def bot_responds(content): # bots reponds function
    col1, col2 = st.columns([12, 1])
    with col1:
        with st.spinner("🚘Processing..."):
            time.sleep(2)
        current_time = datetime.now().strftime('%I:%M:%S %p')
        st.session_state.messages.append({"role": "bot", "content": content, 'time':current_time})
def img_to_base64(image_path): # image displaying
    """Convert image to base64."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        logging.error(f"Error converting image to base64: {str(e)}")
        return None

st.markdown('<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">', unsafe_allow_html=True) #open sans font google link

def display_user_message(message, time, img_base64): # user message displaying function
    # Align user message on the left and user icon on the right
    st.markdown(f"""
    <div style="display: flex; justify-content: flex-end; align-items: center; margin-bottom: 10px;">
        <div style="border: 2px solid #3bc5f1; padding: 10px; border-radius: 10px; max-width: 70%; margin-right: -55px; margin-bottom: 22px; font-size: 12x;">
            <p style="margin: 0; font-size: 10px; color: #B0BEC5; font-family: "Open Sans", sans-serif;">{time}</p>
            <p style="margin: 0; font-size: 12px; color:  #455A64 ; font-family: "Open Sans", sans-serif;">{message}</p>    
        </div>
        <div style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; margin-left: 38px; margin-top: -50px;">
            <img src="data:image/jpeg;base64,{img_base64}" alt="User Icon" style="width: 30px; height: 30px; object-fit: cover; margin-left: 38px;"/>
        </div>
    </div>
    """, unsafe_allow_html=True)

def reset_interaction(): # refresh function
    expander_open = st.session_state.get("expander_open", True)
    st.session_state.clear()
    st.session_state.expander_open = expander_open  
    st.session_state.step = 'initial'
    st.session_state.render_start_button = True


def display_uploaded_imagenow(file): # displaying the image 
    img = Image.open(file)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    base64_image = base64.b64encode(img_bytes.getvalue()).decode("utf-8")
    return base64_image


def create_pdf(vehicle_image_path): # creating quotation pdf 
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=16, style="B")
    pdf.set_text_color(255, 99, 71)  
    pdf.cell(200, 10, txt="Insurance Quotation", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)  
    pdf.cell(200, 10, txt=f"Quotation ID: {st.session_state.quotation_id}", ln=True, align="L")


    pdf.set_font("Arial", size=14, style="B")
    pdf.set_text_color(255, 99, 71)  
    pdf.cell(200, 10, txt="Personal Details", ln=True, align="L")
    pdf.set_font("Arial", size=12)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.set_text_color(0, 0, 0)  
    pdf.cell(200, 10, txt=f"Name: {st.session_state.user_data.get('full_name', 'Name not provided')}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Age: {st.session_state.user_data.get('age', 'Age not provided')}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Address: {st.session_state.user_data.get('Address', 'State not selected')}", ln=True, align="L")

    pdf.set_font("Arial", size=14, style="B")
    pdf.set_text_color(255, 99, 71) 
    pdf.cell(200, 10, txt="Vehicle Details", ln=True, align="L")
    pdf.set_font("Arial", size=12)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.set_text_color(0, 0, 0) 
    pdf.cell(200, 10, txt=f"License Number: {st.session_state.user_data.get('license_no', 'Not provided')}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Your's VIN: {st.session_state.user_data.get('vin_number', 'Not provided')}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Make: {st.session_state.user_data.get('make', 'Not provided')}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Model: {st.session_state.user_data.get('model', 'Not provided')}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Year: {st.session_state.user_data.get('model_year', 'Not provided')}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Date of Purchase: {st.session_state.user_data.get('date', 'Not provided')}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Fuel Type: {st.session_state.user_data.get('fuel_type', 'Not provided')}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Primary Use: {st.session_state.user_data.get('primary_use', 'Not provided')}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Deductible Amount: {st.session_state.user_data.get('deductible_range', 'Not provided')}", ln=True, align="L")


    x_vehicle = 100  
    y_vehicle = pdf.get_y() - 80  
    pdf.image(vehicle_image_path, x=x_vehicle, y=y_vehicle, w=100)

    pdf.set_font("Arial", size=14, style="B")
    pdf.set_text_color(255, 99, 71)  # Set color to #FF6347
    pdf.cell(200, 10, txt="Risk Evaluation", ln=True, align="L")
    pdf.set_font("Arial", size=12)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.set_text_color(0, 0, 0)  # Reset color to black
    pdf.set_font("Arial", style="B", size=12)  # Set font to Arial, bold, and size 12
    pdf.cell(200, 10, txt=f"Risk Category: {st.session_state.user_data.get('output', 'Not provided')}", ln=True, align="L")
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Explanation:\n 1.Total claims: {st.session_state.user_data.get('total_claims', 'Not provided')} \n 2.Odometer range: {st.session_state.user_data.get('odoo_range', 'Not provided')}")
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt=f"Premium amount: {st.session_state.user_data.get('risk_amount', 'Not provided')}", ln=True, align="L")


    pdf.set_y(-40)  
    pdf.set_font("Arial", size=8)  
    disclaimer_text = (
        "Disclaimer: This is a sample auto insurance quote generated based on the provided details. "
        "The actual premium may vary based on additional factors such as driving history, claim records, "
        "and insurance provider terms."
    )
    pdf.multi_cell(0, 5, txt=disclaimer_text, align="C")

    return pdf
def display_license_image(file, width=400): # diplaying the license image
    # Ensure the file is not empty
    if file is None:
        st.error("No file uploaded.")
        return
    
    if file.size == 0:
        st.error("Uploaded file is empty.")
        return
    
    if 'new_images' not in st.session_state:
        st.session_state.new_images = []
        
    try:
        with fitz.open(file) as doc:
            num_pages = doc.page_count
            for page_number in range(num_pages):
                page = doc[page_number]
                pix = page.get_pixmap() 
                img_data = pix.tobytes("png")  
                st.image(img_data, width=300) 
    except Exception as e:
        st.error(f"Error opening PDF: {e}")

def close_expander(): # closing the expander 
    st.session_state.expander_open = False
    st.rerun()
######
# virtual assistant functions coding ends
######

img_path_tiny = "Auto_Quote_Bot.png"
img_base64_tiny = img_to_base64(img_path_tiny)# Convert image to Base64
# Displaying a simple instruction message below the header
st.markdown('<div class="assistant-message">Click below</div>', unsafe_allow_html=True)
# virtual assistant coding star
with st.expander("", icon=":material/chat_bubble:",  expanded=st.session_state.expander_open): # Expander section to show the bot's image, title, and buttons (refresh and close)
    st.session_state.expander_open = True
    col1, col2, col3 = st.columns([6, 1, 1 ]) # Create columns for layout
    with col1:# Display bot logo in the first column
        st.markdown(
            f'<img style="width: 135px; height: 50px; margin-top: -59px; margin-left: -9px;" src="data:image/png;base64,{img_base64_tiny}">',
            unsafe_allow_html=True,
        )

    with col2: # Refresh button in the third column
        st.button("", icon=":material/refresh:", key="refresh_button", on_click=reset_interaction)
    
    with col3: # Close button in the fourth column
        if st.button("", icon=":material/close:", key="close_button"):
            st.session_state.expander_open = False
            st.rerun()
    st.markdown('<div class="first-divider"></div>', unsafe_allow_html=True) # first border lines displayed 
    with st.container(height=383):  # Container to hold chat history
        
        for message in st.session_state.messages:  # Loop to display messages from the chat history
            if message['role'] == 'bot': # role is bot checking
                st.chat_message("assistant").markdown(
                    f"""
                    <div style="display: flex; flex-direction: column; align-items: flex-start;">
                        <div style="border-radius: 10px; color: #455A64; font-family: 'Open Sans', sans-serif; background-color: #eceef1; padding: 10px; word-wrap: break-word;">
                            <span style="font-size: 10px; color: #B0BEC5;">{message['time']}</span><br>
                            <div style="margin-top: 5px; font-size: 12px;">{message['content']}</div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                img_path = "streamlit_user_icon.png" # user icon 
                img_base64 = img_to_base64(img_path) #converting image into base64
                if img_base64:
                    display_user_message(message['content'], message['time'], img_base64)# Display user message

        if st.session_state.step == 'initial': # Checking if the current step is 'initial' to initiate user interaction
            col1, col2 = st.columns([1, 27]) # Creating two columns for layout in the UI
            with col2: # Working with the second column layout
                if st.button("Continue"): # Displaying a continue button and checking if it is clicked
                    current_time = datetime.now().strftime('%I:%M:%S %p') # Getting current time in a 12-hour format
                    st.session_state.messages.append({"role": "human", "content": "Continue", "time": current_time}) # Adding message to session state
                    st.session_state.name_shown = True # Setting the flag to show name input
                    st.session_state.text_shown = True # Setting flag to show text
                    st.session_state.message_shown = True # Indicating that the message is shown
                    st.session_state.show_progress_bar = True # Enabling progress bar visibility
                    st.session_state.progress = 5 # Setting initial progress value
                    st.session_state.step = 'name' # Changing step to 'name' for further interaction
                    st.rerun() # Rerun to refresh the app and apply changes

        elif st.session_state.step == 'name': # If step is 'name', instructing the user to upload a Driver's License
            bot_responds("Upload your Driver's License") # Bot's response asking for a Driver's License upload
            st.session_state.step = 'get_name' # Changing step to 'get_name' after bot's response
            st.rerun() # Rerun the app to reflect the new step

        elif st.session_state.step == 'get_name': # Step to handle the uploaded PDF file (Driver's License)
            current_time = datetime.now().strftime('%I:%M:%S %p') # Get the current time in 12-hour format
            col1, col2 = st.columns([1, 25]) # Creating two columns layout for file uploader
            with col2: # Handling the second column where file uploader will be placed
                uploaded_file = st.file_uploader("", type="pdf") # File uploader for PDF files
            if uploaded_file is not None: # Checking if the file is uploaded
                st.session_state.pdf_file = uploaded_file # Saving uploaded file to session state
                file_name = uploaded_file.name # Extracting the uploaded file's name
                st.session_state["file_name"] = file_name # Saving file name to session state
                current_time = datetime.now().strftime('%I:%M:%S %p') # Get the current time
                st.session_state.messages.append({"role": "human", "content": "Uploaded Driver's License", "time": current_time}) # Adding the uploaded message to chat history
                st.session_state.license_uploaded = True # Setting flag to indicate that the license is uploaded
                st.session_state.step = 'get_company_name' # Changing step to 'get_company_name'
                st.rerun() # Rerun to process the next step

        elif st.session_state.step == 'get_company_name': # Handling company name input or default response based on file
            if user_input := st.session_state.get('chat_input'): # Checking if there's a user input in session state
                current_time = datetime.now().strftime('%I:%M:%S %p') # Get current time
                st.session_state.messages.append({"role": "human", "content": user_input, "time": current_time}) # Adding user input to messages
                st.session_state.user_data['age'] = user_input # Storing user input as age in user data
                st.rerun() # Rerun to reflect changes in the session state

            if not user_input and len(st.session_state.messages) > 0 and st.session_state.messages[-1]['role'] == 'human': # Checking if no input but messages are available
                file_name_now = st.session_state.get("file_name") # Extracting the file name from session state
                if file_name_now == 'John_doe_license.pdf': # Checking if file name matches a specific case
                    bot_responds("""<p><b>Here are the Driver's details</b></p><p><b>Full Name:</b> John Doe</p><p><b>Age:</b> 32</p><p><b>DOB:</b> 09-05-1993</p><p><b>Gender:</b> Male</p><p><b>Driver's License#:</b> 123456789</p><p><b>Address:</b> 0123 ANYSTREET, ANYTOWN, CA012345</p>""") # Responding with user details from uploaded license
                    st.session_state.user_data.update({"full_name": 'John Doe', "age": '32', "dob": '09-05-1993', "Gender": 'Male', "license_no": '123456789', "Address": '0123 ANYSTREET, ANYTOWN, CA012345'}) # Updating user data with extracted details
                    st.session_state.progress = 30 # Setting progress to 30% after response
                    st.session_state.step = 'select_services_now' # Changing step to 'select_services_now'
                    st.rerun() # Rerun to proceed to next step
                elif file_name_now == 'John_sample_license.pdf': # Another specific file case
                    bot_responds("""<p><b>Here are the Driver's details</b></p><p><b>Full Name:</b> John Sample</p><p><b>Age:</b> 42</p><p><b>DOB:</b> 08-12-1983</p><p><b>Gender:</b> Female</p><p><b>Driver's License#:</b> 10003432</p><p><b>Address:</b> 12 Cottonwood RD East, Texas Center, Texas 12345-0000</p>""") # Responding for 'John_sample_license.pdf'
                    st.session_state.user_data.update({"full_name": 'John Sample', "age": '42', "dob": '08-12-1983', "Gender": 'Female', "license_no": '10003432', "Address": '12 Cottonwood RD East, Texas Center, Texas 12345-0000'}) # Updating user data for 'John Sample'
                    st.session_state.progress = 30 # Setting progress to 30%
                    st.session_state.step = 'select_services_now' # Moving to the next step
                    st.rerun() # Rerun to proceed to next step
                elif file_name_now == 'janice_sample_license.pdf': # Another specific file case
                    bot_responds("""<p><b>Here are the Driver's details</b></p><p><b>Full Name:</b> Janice Sample</p><p><b>Age:</b> 58</p><p><b>DOB:</b> 01-12-1967</p><p><b>Gender:</b> Female</p><p><b>Driver's License#:</b> S000123456789</p><p><b>Address:</b> 123 North Main Street, Lansing, Michigan 48918-1234</p>""") # Responding for 'janice_sample_license.pdf'
                    st.session_state.user_data.update({"full_name": 'Janice Sample', "age": '58', "dob": '01-12-1967', "Gender": 'Female', "license_no": 'S000123456789', "Address": '123 North Main Street, Lansing, Michigan 48918-1234'}) # Updating user data for 'Janice Sample'
                    st.session_state.progress = 30 # Setting progress to 30%
                    st.session_state.step = 'select_services_now' # Moving to the next step
                    st.rerun()
        elif st.session_state.step == 'select_services_now':  # Checking if the current step is 'select_services_now'
            col1, col2 = st.columns([1, 25])  # Creating two columns layout for the user interface
            with col2:  # Working with the second column layout
                st.empty()  # Creating an empty space in the layout (for aesthetics or placeholder)
                if st.button("Proceed with VIN"):  # Displaying the button and checking if it is clicked
                    current_time = datetime.now().strftime('%I:%M:%S %p')  # Getting current time in 12-hour format
                    st.session_state.messages.append({"role": "human", "content": "VIN", "time": current_time})  # Logging the button click in messages
                    st.session_state.name_shown = True  # Indicating that the name is shown
                    st.session_state.step = 'select_services'  # Changing step to 'select_services'
                    st.rerun()  # Rerun the app to apply changes

        elif st.session_state.step == 'select_services':  # Checking if the current step is 'select_services'
            bot_responds("Enter your VIN")  # Bot responds asking the user to enter their VIN
            st.session_state.step = 'next_step'  # Moving to the 'next_step'
            st.rerun()  # Rerun the app to reflect the new step

        elif st.session_state.step == 'next_step':  # Handling the step after VIN is entered
            if user_input := st.session_state.get('chat_input'):  # Checking if there is user input
                if re.fullmatch(r'^[A-Za-z0-9]{17}$', user_input):  # Checking if the VIN matches the required format (17 alphanumeric characters)
                    st.session_state.user_data["vin_number"] = user_input  # Saving VIN to user data
                    current_time = datetime.now().strftime('%I:%M:%S %p')  # Getting current time
                    st.session_state.messages.append({"role": "human", "content": f"{user_input}", "time": current_time})  # Logging the VIN input
                    st.session_state.step = 'selected_city_now'  # Changing the step to 'selected_city_now'
                    st.session_state["email_error"] = ""  # Clearing any previous email errors
                    st.rerun()  # Rerun to apply changes

                else:  # If the VIN doesn't match the required format
                    st.session_state.email_error = "<span style='color:red; margin-left:25px;'>Please enter a valid VIN.</span>"  # Displaying error message for invalid VIN
                    if st.session_state.email_error:  # Checking if there's an error message
                        st.markdown(st.session_state.email_error, unsafe_allow_html=True)  # Displaying error message in HTML format

        elif st.session_state.step == 'selected_city_now':  # Handling the step after VIN is successfully validated
            file_name_now = st.session_state.get("file_name")  # Extracting the uploaded file name from session state
            if file_name_now == 'John_doe_license.pdf':  # Checking if the uploaded file is 'Johnson_robert_license.pdf'
                bot_responds("""<p><b>Here are the your vehicle details</b></p><p><b>Make:</b> BMW</p><p><b>Model:</b> 3 Series</p><p><b>Year:</b> 2024</p><p><b>Vehicle Type:</b> Diesel</p>""")  # Bot responds with vehicle details
                st.session_state.user_data.update({"make": 'BMW', "model": '3 Series', "model_year": '2024', "fuel_type": 'Diesel', "output": 'High', "risk_amount": '$1916.00'})  # Saving vehicle data to session state
                st.session_state.progress = 50  # Updating the progress to 50%
                st.session_state.step = 'selected_model_now'  # Moving to the next step 'selected_model_now'
                st.rerun()  # Rerun the app to apply changes
            elif file_name_now == 'John_sample_license.pdf':  # Checking if the uploaded file is 'John_sample_license.pdf'
                bot_responds("""<p><b>Here are the your vehicle details</b></p><p><b>Make:</b> BMW</p><p><b>Model:</b> 5 Series</p><p><b>Year:</b> 2024</p><p><b>Vehicle Type:</b> Petrol</p>""")  # Responding with vehicle details for 'John_sample_license.pdf'
                st.session_state.user_data.update({"make": 'BMW', "model": '5 Series', "model_year": '2024', "fuel_type": 'Petrol', "output": 'High', "risk_amount": '$23.32'})  # Saving vehicle data to session state
                st.session_state.progress = 50  # Updating the progress to 50%
                st.session_state.step = 'selected_model_now'  # Moving to the next step 'selected_model_now'
                st.rerun()  # Rerun to apply changes
            elif file_name_now == 'janice_sample_license.pdf':  # Checking if the uploaded file is 'janice_sample_license.pdf'
                bot_responds("""<p><b>Here are the your vehicle details</b></p><p><b>Make:</b> BMW</p><p><b>Model:</b> i3</p><p><b>Year:</b> 2024</p><p><b>Vehicle Type:</b> Electric</p>""")  # Responding with vehicle details for 'janice_sample_license.pdf'
                st.session_state.user_data.update({"make": 'BMW', "model": 'i3', "model_year": '2024', "fuel_type": 'Electric', "output": 'Low', "risk_amount": '$31.32'})  # Saving vehicle data to session state
                st.session_state.progress = 50  # Updating the progress to 50%
                st.session_state.step = 'selected_model_now'  # Moving to the next step 'selected_model_now'
                st.rerun()  # Rerun to apply changes
        elif st.session_state.step == 'selected_model_now':  # Checking if the current step is 'selected_model_now'
            col1, col2 = st.columns([1, 25])  # Creating two column layout for the user interface
            with col2:  # Working with the second column layout
                if st.button("Vehicle Photo"):  # Displaying the button and checking if it is clicked
                    current_time = datetime.now().strftime('%I:%M:%S %p')  # Getting current time in 12-hour format
                    st.session_state.messages.append({"role": "human", "content": "Vehicle Photo", "time": current_time})  # Logging the button click in messages
                    st.session_state.name_shown = True  # Indicating that the name is shown
                    st.session_state.step = 'select_car_image'  # Changing step to 'select_car_image'
                    st.rerun()  # Rerun the app to apply changes

        elif st.session_state.step == 'select_car_image':  # Checking if the current step is 'select_car_image'
            bot_responds("Upload your vehicle photo")  # Bot responds asking the user to upload a vehicle photo
            st.session_state.step = 'image_show'  # Moving to the 'image_show' step
            st.rerun()  # Rerun the app to apply changes

        elif st.session_state.step == 'image_show':  # Handling the step where the image upload happens
            col1, col2 = st.columns([1, 25])  # Creating two column layout for the user interface
            with col2:  # Working with the second column layout
                uploaded_image = st.file_uploader(  # Allowing user to upload an image file with specific file types
                    "", 
                    type=["png"]
                )
            if uploaded_image is not None and st.session_state.image_file is None:  # Checking if an image is uploaded and no image has been set in session state
                st.session_state.image_file = uploaded_image  # Saving the uploaded image to session state
                image_vehicle = uploaded_image.name  # Extracting the image name
                st.session_state["image_vehicle"] = image_vehicle  # Storing image name in session state
                # display_uploaded_image(st.session_state.image_file)  # Optionally, display the uploaded image (function is commented out)
                current_time = datetime.now().strftime('%I:%M:%S %p')  # Getting current time in 12-hour format
                st.session_state.messages.append({"role": "human", "content": "Uploaded Vehicle Photo", "time": current_time})  # Logging the image upload
                st.session_state.license_uploaded = False  # Indicating that the license image is not uploaded anymore
                st.session_state.image_uploaded = True  # Indicating that the vehicle image is uploaded
                st.session_state.progress = 60  # Updating progress to 60%
                st.session_state.step = 'select_date_msg'  # Changing step to 'select_date_msg'
                st.rerun()  # Rerun the app to apply changes

        elif st.session_state.step == 'select_date_msg':  # Checking if the current step is 'select_date_msg'
            bot_responds("Date of Purchase")  # Bot responds asking for the date of purchase
            st.session_state.step = 'date_show'  # Moving to the 'date_show' step
            st.rerun()  # Rerun the app to apply changes

        elif st.session_state.step == 'date_show':  # Handling the step where the user inputs the date of purchase
            col1, col2 = st.columns([1, 25])  # Creating two column layout for the user interface
            with col2:  # Working with the second column layout
                if 'date' not in st.session_state:  # Checking if 'date' key is not in session state
                    st.session_state.date = None  # Initializing 'date' as None if not present
                
                selected_date = st.date_input(  # Allowing user to select a date from a date picker
                    "", 
                    key="date", 
                    label_visibility="visible", 
                    value=st.session_state.date, 
                    max_value=date.today()  # Setting the maximum date value as today
                )

                if selected_date:  # If the user selects a date
                    formatted_date = selected_date.strftime('%m-%d-%Y')  # Formatting the selected date
                    st.session_state.user_data['date'] = formatted_date  # Saving formatted date to user data
                    current_time = datetime.now().strftime('%I:%M:%S %p')  # Getting current time in 12-hour format
                    st.session_state.messages.append({"role": "human", "content": f"{formatted_date}", "time": current_time})  # Logging the selected date
                    st.session_state.progress = 70  # Updating progress to 70%
                    st.session_state.step = 'selected_date_now'  # Moving to the 'selected_date_now' step
                    st.rerun()  # Rerun the app to apply changes
        elif st.session_state.step == 'selected_date_now':  # Checking if the current step is 'selected_date_now'
            bot_responds("What's your Odometer range")  # Bot prompts the user to input the odometer range
            st.session_state.step = 'selected_date'  # Moving to the next step 'selected_date'
            st.rerun()  # Rerun the app to apply changes

        elif st.session_state.step == 'selected_date':  # Handling the step where the user selects the odometer range
            ranges = [  # Defining possible odometer ranges
                "0-5000", "5000-10000", "10000-50000", "50000-100000", "100000-150000", "150000-200000"
            ]
            col1, col2 = st.columns([1, 25])  # Creating two column layout for the user interface
            with col2:  # Working with the second column layout
                odometer_range = st.selectbox(  # Displaying a select box for the user to pick an odometer range
                    "", 
                    options=["Select a range"] + ranges,  # Adding a default "Select a range" option
                    key='odometer_selection'
                )

            if odometer_range != "Select a range":  # Checking if the user has selected a valid range
                st.session_state.user_data['odoo_range'] = odometer_range  # Saving the selected range to user data
                current_time = datetime.now().strftime('%I:%M:%S %p')  # Getting current time in 12-hour format
                st.session_state.messages.append({"role": "human", "content": f"{odometer_range}", "time": current_time})  # Logging the selected range
                st.session_state.progress = 80  # Updating progress to 80%
                st.session_state.step = 'show_total'  # Moving to the 'show_total' step
                st.rerun()  # Rerun the app to apply changes

        elif st.session_state.step == 'show_total':  # Checking if the current step is 'show_total'
            bot_responds("How many claims made till date")  # Bot prompts the user to input total claims made
            st.session_state.step = 'show_total_no'  # Moving to the 'show_total_no' step
            st.rerun()  # Rerun the app to apply changes

        elif st.session_state.step == 'show_total_no':  # Handling the step where the user selects the number of claims made
            col1, col2 = st.columns([1, 25])  # Creating two column layout for the user interface
            with col2:  # Working with the second column layout
                options_total = ["1-3", "3-7", "7-10"]  # Defining claim ranges
                selection_total = st.pills("", options_total)  # Allowing the user to select a claim range using pills

            if selection_total:  # Checking if the user has selected a claim range
                current_time = datetime.now().strftime('%I:%M:%S %p')  # Getting current time in 12-hour format
                st.session_state.messages.append({"role": "human", "content": f"{selection_total}", "time": current_time})  # Logging the selected claim range
                st.session_state.progress = 85  # Updating progress to 85%
                st.session_state.step = 'total_deductible'  # Moving to the 'total_deductible' step
                st.session_state.user_data['total_claims'] = selection_total  # Saving the selected claim range to user data
                st.rerun()  # Rerun the app to apply changes

        elif st.session_state.step == 'total_deductible':  # Checking if the current step is 'total_deductible'
            bot_responds("Select your deductible amount")  # Bot prompts the user to select a deductible amount
            st.session_state.step = 'total_deductible_values'  # Moving to the 'total_deductible_values' step
            st.rerun()  # Rerun the app to apply changes

        elif st.session_state.step == 'total_deductible_values':  # Handling the step where the user selects the deductible amount
            ranges_deduct = [  # Defining available deductible amounts
                "$1,000", "$2,000", "$3,000", "$4,000", "$5,000"
            ]
            col1, col2 = st.columns([1, 25])  # Creating two column layout for the user interface
            with col2:  # Working with the second column layout
                deduct_range = st.selectbox(  # Displaying a select box for the user to pick a deductible amount
                    "", 
                    options=["Select a amount"] + ranges_deduct,  # Adding a default "Select an amount" option
                    key='deductible_selection'
                )

            if deduct_range != "Select a amount":  # Checking if the user has selected a valid deductible amount
                st.session_state.user_data['deductible_range'] = deduct_range  # Saving the selected deductible to user data
                current_time = datetime.now().strftime('%I:%M:%S %p')  # Getting current time in 12-hour format
                st.session_state.messages.append({"role": "human", "content": f"{deduct_range}", "time": current_time})  # Logging the selected deductible
                st.session_state.progress = 90  # Updating progress to 90%
                st.session_state.step = 'show_quotation_now'  # Moving to the 'show_quotation_now' step
                st.rerun()  # Rerun the app to apply changes

        elif st.session_state.step == 'show_quotation_now':  # Checking if the current step is 'show_quotation_now'
            bot_responds("Select the usage type")  # Bot prompts the user to select the vehicle's usage type
            st.session_state.step = 'primary_use'  # Moving to the 'primary_use' step
            st.rerun()  # Rerun the app to apply changes

        elif st.session_state.step == 'primary_use':  # Handling the step where the user selects the usage type
            col1, col2 = st.columns([1, 25])  # Creating two column layout for the user interface
            with col2:  # Working with the second column layout
                primary_use_commuting = st.checkbox("Commuting", key="commuting_use")
                primary_use_personal = st.checkbox("Personal", key="personal_use")
                primary_use_business = st.checkbox("Business", key="business_use")

                # Collect the selected primary uses
                primary_use = []
                if primary_use_commuting:
                    primary_use.append("Commuting")
                if primary_use_personal:
                    primary_use.append("Personal")
                if primary_use_business:
                    primary_use.append("Business")

            if primary_use:  # Checking if the user has selected at least one usage type
                selected_uses = ", ".join(primary_use)  # Joining selected usage types into a single string
                st.session_state.user_data['primary_use'] = selected_uses  # Saving selected usage types to user data
                current_time = datetime.now().strftime('%I:%M:%S %p')  # Getting current time in 12-hour format
                st.session_state.messages.append({"role": "human", "content": f"{selected_uses}", "time": current_time})  # Logging selected usage types
                st.session_state.step = 'show_quotation_final'  # Moving to the 'show_quotation_final' step
                st.rerun()  # Rerun the app to apply changes

        elif st.session_state.step == 'show_quotation_final':  # Checking if the current step is 'show_quotation_final'
            bot_responds("Thank You for your time and patience, your quote is being generated, kindly check out on your main page...")  # Final bot response thanking the user
            st.markdown(
                """
                <div style="font-size:60px; color:rgb(41 105 183);">
                    <span class="material-icons">north_west</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.session_state.progress = 100  # Updating progress to 95%
            st.session_state.step = 'show_quotation'  # Moving to the 'show_quotation' step
            st.session_state.image_uploaded = False  # Resetting image upload status
            st.rerun()  # Rerun the app to apply changes


        # Checking if the step is not one of the predefined steps, and if the chat input is visible
        if st.session_state.step not in ['initial','name','get_name','get_company_name','select_services_now','select_services','selected_city_now','selected_model_now','select_car_image',
                'image_show','select_date_msg','date_show','selected_date_now','selected_date','show_total','show_total_no','total_deductible','total_deductible_values','show_quotation_now','primary_use','show_quotation_final','show_quotation'] and st.session_state.get('chat_input_visible', True):
            col1, col2 = st.columns([1, 20])  # Creating two column layout for the user interface
            with col2:  # Working with the second column layout
                user_input = st.chat_input("Type your message", key="chat_input")  # Allowing the user to type a message in the chat input box
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)  # Adding a divider for layout separation
    st.markdown('<div class="powered-by">Powered By BotDNA</div>', unsafe_allow_html=True)  # Displaying a footer with the "Powered by BotDNA" message
# virtual assistant coding ends

# Auto insurance quote header with styling
if nav == ':blue[Auto Quote]':
    # Displaying a welcome header with styling
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600&display=swap');
        </style>
        <h1 style='text-align: center; color: rgb(41 105 183); font-size:20px; margin-left:-274px; margin-top:-63px; font-family: "Open Sans", sans-serif;'>
                Welcome to Auto Quote Bot🚘
        </h1>
        <div style='width: 43%; border-top: 2px solid rgb(41 105 183); margin-top: -11px; margin-left: 48px;'></div>
    """, unsafe_allow_html=True)

    if not st.session_state.text_shown: # Checking if the text has not been shown yet
        # Displaying some introductory information about the AI-powered Quote Generator using Markdown
        st.markdown("""
        <ul style='color: 333; font-size: 14px;  margin-top:25px; margin-left:-33px; font-family: "Open Sans", sans-serif;'>
        Our AI-powered Quote Generator is designed to provide you with quick, accurate, and personalized auto insurance quotes in just a few clicks. Whether you're a first-time buyer or looking to switch providers, BotDNA makes the process seamless and stress-free.
        </ul>

        <h5 style='margin-left: -33px; color:rgb(41 105 183); font-family: "Open Sans", sans-serif; font-size: 16px;'>Key Features</h5>
        <ul style='margin-left: -33px; color:333; font-family: "Open Sans", sans-serif; font-size: 14px;'>
            <li><b>Instant Quotes</b>: Get real-time auto insurance quotes based on your unique profile.</li>
            <li><b>User-Friendly Interface</b>: Our app is designed to be intuitive and easy to navigate, making the quote generation process a breeze.</li>
            <li><b>Secure and Confidential</b>: Your data is safe with us. We use advanced encryption to protect your personal information.</li>
        </ul>
        <h5 style='margin-left: -33px; color:rgb(41 105 183); font-family: "Open Sans", sans-serif; font-size: 14px;'>How to Use the App</h5>
        <ul style='margin-left: -33px; color:333; font-family: "Open Sans", sans-serif; font-size: 14px; '>
            <li><b>Enter Your Details</b>: Start by entering your personal and vehicle details.</li>
            <li><b>Get Your Quote</b>:  Our AI will analyze your data and generate a quote based on risk evaluation.</li>
            <li><b>Download the Quote</b>: You can download the quote directly as a pdf.</li>
        </ul>
                    
        <h1 style='text-align: center; color: rgb(41 105 183); font-family: "Open Sans", sans-serif; margin-left: -284px; font-size: 20px;'>Click on the Bot to continue.</h1>
        """, unsafe_allow_html=True) # Displaying text, key features, and instructions in styled HTML
    col1, col2, col3 = st.columns([3, 1, 1])  # Creating a 3-column layout for progress and other content
    with col1:
        if st.session_state.show_progress_bar:  # Check if progress bar is visible
            progress = st.session_state.progress  # Get the current progress value
            if progress == 5: progress_text = f"{progress}% Initializing..."  # Setting text based on progress value
            elif progress == 30: progress_text = f"{progress}% Making steady progress..."
            elif progress == 50: progress_text = f"{progress}% Halfway through..."
            elif progress == 60: progress_text = f"{progress}% Processing..."
            elif progress == 70: progress_text = f"{progress}% Doing great..."
            elif progress == 80: progress_text = f"{progress}% You are Almost there..."
            elif progress == 85: progress_text = f"{progress}% Just a little more..."
            elif progress == 90: progress_text = f"{progress}% Wrapping things up..."
            elif progress == 100: progress_text = f"{progress}% Completed!"  # Default case for progress text
            else: progress_text = f"{progress}%"  # For undefined progress values
            progress_placeholder = st.empty()  # Create a placeholder
            my_bar = progress_placeholder.progress(progress, text=progress_text)

            if progress == 100:
                time.sleep(2)  # Pause to allow the user to see the final message
                progress_placeholder.empty()  # Clear the progress bar
                st.session_state.show_progress_bar = False  # Disable the progress bar


        if st.session_state.license_uploaded:  # If a license image is uploaded, display it
            display_license_image(st.session_state.pdf_file)  # Function to display license image

        if st.session_state.image_uploaded:  # If a car image is uploaded, display it
            img_car = st.session_state.image_file  # Get the uploaded car image
            st.image(img_car, width=280)  # Display car image with a width of 280px


        
            
    col_left, col_right = st.columns([1, 1], gap="large")# Creating two columns for displaying content, with a large gap between them
    with col_left:
        if st.session_state.step == 'show_quotation':  # Check if the current step is 'show_quotation'
            if st.session_state.show_progress_bar:  # Check if the progress bar is visible
                st.session_state.progress = 100  # Ensure the progress is complete
                st.session_state.show_progress_bar = False  # Disable the progress bar
                st.empty()
            if not st.session_state.quotation_shown:  # Check if the quotation has already been shown
                with st.spinner("🚘Please wait."):  # Show a loading spinner
                    time.sleep(3)  # Simulate processing delay
                st.session_state.quotation_shown = True  # Set quotation as shown
            fuel_type = st.session_state.user_data.get('fuel_type', '')  # Get the fuel type of the vehicle
            if fuel_type == 'Electric' or fuel_type == 'Hybrid':  # If the vehicle is Electric or Hybrid
                # Injecting custom CSS styles for quotation container
                st.markdown(
                    """
                    <style>
                    .custom-container {
                        height: 600px
                        width: 400px;
                        padding: 20px;
                        margin: 0 auto;
                        border: 2px solid #2969B7;
                        font-family: Arial, sans-serif;
                    }
                    .custom-container-risk {
                        border: 2px solid #2969B7;  /* Tomato color for a clear box */
                        padding: 15px;
                        background-color: #f9f9f9;
                        border-radius: 10px;
                        text-align: left;
                        margin-left: -235px; /* Adjust the container's horizontal position */
                        width: 662px; /* Set the desired width */
                        height: 555px; /* Set the desired height */
                        /* Add scrollbars if content overflows */
                    }
                    .risk-evaluation {
                        font-size: 18px;
                        font-weight: bold;
                        color: #2969B7;  /* Matching the border color */
                    }
                    .divider-risk {
                        height: 2px;
                        background-color: #2969B7;
                        margin-top: 10px;
                        margin-bottom: 15px;
                    }
                    .personal-details {
                        font-size: 18px;
                        font-weight: bold;
                        color: #2969B7; 
                    }
                    .vehicle-details {
                        font-size: 18px;
                        font-weight: bold;
                        color: #2969B7; 
                    }
                    .vehicle-image {
                        width: 35%;
                        margin-left: 400px;
                        margin-top: -250px
                    }
                    .deductible-details {
                        font-size: 18px;
                        font-weight: bold;
                        color: #2969B7; 
                    }
                    .quotation-id {
                        text-align: right;
                        width: 100%;
                        margin-top: -30px
                    }
                    .download-button {
                        margin-top: 10px;
                    }
                    # .hidden-content {
                    #     display: none;
                    # }
                    .show-more:checked + .hidden-content {
                        display: block;
                    }
                    .show-more-label {
                        color: black;
                        cursor: pointer;
                    }
                    .spinner-container {
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        margin-top: -20px;
                        margin-left: -800px;
                    }

                    .spinner {
                        animation: spin 3s linear forwards;
                    }

                    @keyframes spin {
                        0% {
                            transform: rotate(0deg);
                        }
                        100% {
                            transform: rotate(360deg);
                        }
                    }

                    .message {
                        font-size: 1rem;
                        color: #333;
                    }
                    .first-container {
                        margin-bottom: 20px;  
                    }
                    
                    
                    </style>
                    """, 
                    unsafe_allow_html=True
                )

                if 'image_file' in st.session_state:  # Check if an image file exists in session state
                    image_file = st.session_state.image_file  # Get the uploaded image file
                    base65_image = display_uploaded_imagenow(image_file)  # Convert image file to base64
                else:
                    base65_image = ""  # If no image uploaded, set it as empty

                current_date = datetime.now()  # Get current date and time
                day = current_date.day  # Get the day from current date
                year = current_date.year  # Get the year from current date
                month = current_date.month  # Get the month from current date
                st.session_state.quotation_id = f"AIG-{year}{month:02d}{day:02d}-001"  # Generate unique quotation ID
                vehicle_image_path = st.session_state["image_vehicle"]  # Get vehicle image path
                pdf = create_pdf(vehicle_image_path)  # Create the PDF with vehicle images
                pdf_output = f"quotation_{st.session_state.quotation_id}.pdf"  # Define the output PDF file name
                pdf.output(pdf_output)  # Save the generated PDF
                with open(pdf_output, "rb") as pdf_file:  # Open the PDF in binary mode
                    pdf_base64 = base64.b64encode(pdf_file.read()).decode('utf-8')  # Convert PDF to base64 format
                # Injecting custom CSS styles for quotation container
                st.markdown(
                    f"""
                    <div class="custom-container-risk first-container">
                        <div class="personal-details">
                            <span>Personal Details(Policy Holder)</span>
                        </div>
                        <div class="quotation-id">
                            <span><b>Auto Quote ID: {st.session_state.quotation_id}</b></span>
                        </div>
                        <div class="divider-risk"></div>
                        <div class="personal-content">
                            <p>{st.session_state.user_data.get('full_name', 'Name not provided')}, aged {st.session_state.user_data.get('age', 'Age not provided')} resides in {st.session_state.user_data.get('Address', 'State not selected')}. She purchased {st.session_state.user_data.get('make', 'Make not provided')} recently.</p>
                        </div>
                        <div class="vehicle-details">
                            <span>Vehicle Details</span>
                        </div>
                        <div class="divider-risk"></div>
                        <div class="vehicle-container">
                            <div class="vehicle-text">
                                <p><strong>Your driver’s license number:</strong> {st.session_state.user_data.get("license_no", 'Name not provided')}</p>
                                <p><strong>Your VIN number:</strong> {st.session_state.user_data.get("vin_number", 'Name not provided')}</p>
                                <p><strong>Make:</strong> {st.session_state.user_data.get('make', 'Name not provided')}</p>
                                <p><strong>Model:</strong> {st.session_state.user_data.get('model', 'Name not provided')}</p>
                                <p><strong>Year:</strong> {st.session_state.user_data.get('model_year', 'Name not provided')}</p>
                                <p><strong>Date of Purchase:</strong> {st.session_state.user_data.get('date', 'Name not provided')}</p>
                                <p><strong>Vehicle Type:</strong> {st.session_state.user_data.get('fuel_type', 'Fuel type not provided')}</p>
                                <p><strong>Primary Use:</strong> {st.session_state.user_data.get('primary_use', 'Primary use not provided')}</p>
                                <p><strong>Deductible Amount:</strong> {st.session_state.user_data.get('deductible_range', 'Primary use not provided')}</p>
                            </div>
                        </div>
                        <div class="vehicle-image">
                                <img src="data:image/png;base64,{base65_image}" alt="Vehicle Image" style="width: 100%;">
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if "show_premium_clicked" not in st.session_state:  # Check if the premium button clicked state is not in session state
                    st.session_state.show_premium_clicked = False  # Set default state for premium click

                if st.button("Show Premium Amount"):  # Show premium amount button
                    st.session_state.expander_open = True  # keep open previous expanders
                    st.session_state.show_premium_clicked = True  # Set the flag for premium clicked
                    st.rerun()  # Rerun the app to refresh and show premium details
                if st.session_state.show_premium_clicked:  # If premium clicked flag is set
                    message = st.chat_message("assistant").markdown("Please wait...")  # Show chat message while processing
                    col1, col2 = st.columns([1, 40])  # Create columns for the premium details
                    with col2:
                        with st.spinner("Processing..."):  # Show spinner while processing
                            time.sleep(3)  # Simulate processing delay
                        message.markdown("Done! Your Quote is ready")  # Display completion message
                    # Injecting custom CSS styles for quotation container
                    st.markdown(
                        f"""
                        <div class="custom-container-risk">
                            <div class="hidden-content">
                                <div class="risk-evaluation">
                                    <span>Risk Evaluation Details</span>
                                </div>
                                <div class="divider-risk"></div>
                                <div class="risk-content">
                                    <div class="risk-details">
                                        <p><strong>Risk Category:</strong> Low</p>
                                        <p><strong>Explanation:</strong></p>
                                        <ul>
                                            <li>The driver’s age is {st.session_state.user_data.get('age', 'Age not provided')}, which aligns with Rule 1 and Rule 2, classifying it as a low-risk factor.</li>
                                            <li>With the vehicle being a {st.session_state.user_data.get('model_year', 'Name not provided')} model, it meets the conditions of Rule 3, indicating a low-risk category.</li>
                                            <li>The total claims fall within {st.session_state.user_data.get('total_claims', 'Claims not provided')}, which qualifies as a low-risk factor according to Rule 6.</li>
                                            <li>The odometer reading lies between {st.session_state.user_data.get('odoo_range', 'Range not provided')}, marking it as a moderate level of usage.</li>
                                            <li>The city, {st.session_state.user_data.get('Address', 'Location not provided')}, is not associated with high traffic or criminal activity, making it a negligible risk factor under Rule 8.</li>
                                            <li>The vehicle's make is {st.session_state.user_data.get('make', 'Name not provided')}, which is categorized as expensive. Its model, {st.session_state.user_data.get('model', 'Name not provided')}, falls into the premium category, but the variant, Plus S, is relatively affordable. As a whole, the vehicle qualify as an expensive car per Rule 9.</li>
                                            <li>Considering all the rules, the overall risk is assessed to be Low.</li>
                                        </ul>
                                        <p><strong> Based on the risk category Low, premium amount $31.32</strong> </p>
                                    </div>
                                </div>
                                <div class="download-button">
                                    <a href="data:application/pdf;base64,{pdf_base64}" download="quotation_{st.session_state.quotation_id}.pdf">
                                        <button>Download Auto Quote as PDF</button>
                                    </a>
                                </div>
                            </div>
                        </div>
                    """,
                    unsafe_allow_html=True
                )
            elif fuel_type == 'Petrol': # If the vehicle is Petrol
                # Injecting custom CSS styles for quotation container
                st.markdown(
                    """
                    <style>
                    .custom-container {
                        height: 600px
                        width: 400px;
                        padding: 20px;
                        margin: 0 auto;
                        border: 2px solid #2969B7;
                        font-family: Arial, sans-serif;
                    }
                    .custom-container-risk {
                        border: 2px solid #2969B7;  /* Tomato color for a clear box */
                        padding: 15px;
                        background-color: #f9f9f9;
                        border-radius: 10px;
                        text-align: left;
                        margin-left: -235px; /* Adjust the container's horizontal position */
                        width: 662px; /* Set the desired width */
                        height: 555px; /* Set the desired height */
                        /* Add scrollbars if content overflows */
                    }
                    .risk-evaluation {
                        font-size: 18px;
                        font-weight: bold;
                        color: #2969B7;  /* Matching the border color */
                    }
                    .divider-risk {
                        height: 2px;
                        background-color: #2969B7;
                        margin-top: 10px;
                        margin-bottom: 15px;
                    }
                    .personal-details {
                        font-size: 18px;
                        font-weight: bold;
                        color: #2969B7; 
                    }
                    .vehicle-details {
                        font-size: 18px;
                        font-weight: bold;
                        color: #2969B7; 
                    }
                    .vehicle-image {
                        width: 35%;
                        margin-left: 400px;
                        margin-top: -250px
                    }
                    .deductible-details {
                        font-size: 18px;
                        font-weight: bold;
                        color: #2969B7; 
                    }
                    .quotation-id {
                        text-align: right;
                        width: 100%;
                        margin-top: -30px
                    }
                    .download-button {
                        margin-top: 10px;
                    }
                    # .hidden-content {
                    #     display: none;
                    # }
                    .show-more:checked + .hidden-content {
                        display: block;
                    }
                    .show-more-label {
                        color: black;
                        cursor: pointer;
                    }
                    .spinner-container {
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        margin-top: -20px;
                        margin-left: -800px;
                    }

                    .spinner {
                        animation: spin 3s linear forwards;
                    }

                    @keyframes spin {
                        0% {
                            transform: rotate(0deg);
                        }
                        100% {
                            transform: rotate(360deg);
                        }
                    }

                    .message {
                        font-size: 1rem;
                        color: #333;
                    }
                    .first-container {
                        margin-bottom: 20px;  
                    }
                    .custom-container-risk-evaluation {
                        border: 2px solid #2969B7;  /* Tomato color for a clear box */
                        padding: 15px;
                        background-color: #f9f9f9;
                        border-radius: 10px;
                        text-align: left;
                        margin-left: -235px; /* Adjust the container's horizontal position */
                        width: 662px; /* Set the desired width */
                        height: 600px; /* Set the desired height */
                        /* Add scrollbars if content overflows */
                    }
                    
                    
                    </style>
                    """, 
                    unsafe_allow_html=True
                )
                

                if 'image_file' in st.session_state:  # Check if an image file exists in session state
                    image_file = st.session_state.image_file  # Get the uploaded image file
                    base65_image = display_uploaded_imagenow(image_file)  # Convert image file to base64
                else:
                    base65_image = ""  # If no image uploaded, set it as empty

                current_date = datetime.now()  # Get current date and time
                day = current_date.day  # Get the day from current date
                year = current_date.year  # Get the year from current date
                month = current_date.month  # Get the month from current date
                st.session_state.quotation_id = f"AIG-{year}{month:02d}{day:02d}-002"  # Generate unique quotation ID
                vehicle_image_path = st.session_state["image_vehicle"]  # Get vehicle image path
                pdf = create_pdf(vehicle_image_path)  # Create the PDF with vehicle images
                pdf_output = f"quotation_{st.session_state.quotation_id}.pdf"  # Define the output PDF file name
                pdf.output(pdf_output)  # Save the generated PDF
                with open(pdf_output, "rb") as pdf_file:  # Open the PDF in binary mode
                    pdf_base64 = base64.b64encode(pdf_file.read()).decode('utf-8')  # Convert PDF to base64 format
                # Injecting custom CSS styles for quotation container

                st.markdown(
                    f"""
                    <div class="custom-container-risk first-container">
                        <div class="personal-details">
                            <span>Personal Details(Policy Holder)</span>
                        </div>
                        <div class="quotation-id">
                            <span><b>Auto Quote ID: {st.session_state.quotation_id}</b></span>
                        </div>
                        <div class="divider-risk"></div>
                        <div class="personal-content">
                            <p>{st.session_state.user_data.get('full_name', 'Name not provided')}, aged {st.session_state.user_data.get('age', 'Age not provided')} resides in {st.session_state.user_data.get('Address', 'State not selected')}. She purchased {st.session_state.user_data.get('make', 'Make not provided')} recently.</p>
                        </div>
                        <div class="vehicle-details">
                            <span>Vehicle Details</span>
                        </div>
                        <div class="divider-risk"></div>
                        <div class="vehicle-container">
                            <div class="vehicle-text">
                                <p><strong>Your driver’s license number:</strong> {st.session_state.user_data.get("license_no", 'Name not provided')}</p>
                                <p><strong>Your VIN number:</strong> {st.session_state.user_data.get("vin_number", 'Name not provided')}</p>
                                <p><strong>Make:</strong> {st.session_state.user_data.get('make', 'Name not provided')}</p>
                                <p><strong>Model:</strong> {st.session_state.user_data.get('model', 'Name not provided')}</p>
                                <p><strong>Year:</strong> {st.session_state.user_data.get('model_year', 'Name not provided')}</p>
                                <p><strong>Date of Purchase:</strong> {st.session_state.user_data.get('date', 'Name not provided')}</p>
                                <p><strong>Vehicle Type:</strong> {st.session_state.user_data.get('fuel_type', 'Fuel type not provided')}</p>
                                <p><strong>Primary Use:</strong> {st.session_state.user_data.get('primary_use', 'Primary use not provided')}</p>
                                <p><strong>Deductible Amount:</strong> {st.session_state.user_data.get('deductible_range', 'Primary use not provided')}</p>
                            </div>
                        </div>
                        <div class="vehicle-image">
                                <img src="data:image/png;base64,{base65_image}" alt="Vehicle Image" style="width: 100%;">
                        </div>
                    </div>
                        """,
                    unsafe_allow_html=True
                )
                if "show_premium_clicked" not in st.session_state:  # Check if the premium button clicked state is not in session state
                    st.session_state.show_premium_clicked = False  # Set default state for premium click

                if st.button("Show Premium Amount"):  # Show premium amount button
                    st.session_state.expander_open = True  # keep open previous expanders
                    st.session_state.show_premium_clicked = True  # Set the flag for premium clicked
                    st.rerun()  # Rerun the app to refresh and show premium details
                if st.session_state.show_premium_clicked:  # If premium clicked flag is set
                    message = st.chat_message("assistant").markdown("Please wait...")  # Show chat message while processing
                    col1, col2 = st.columns([1, 40])  # Create columns for the premium details
                    with col2:
                        with st.spinner("Processing..."):  # Show spinner while processing
                            time.sleep(3)  # Simulate processing delay
                        message.markdown("Done! Your Quote is ready")  # Display completion message
                    # Injecting custom CSS styles for quotation container
                    st.markdown(
                        f"""
                        <div class="custom-container-risk-evaluation">
                            <div class="risk-evaluation">
                                <span>Risk Evaluation Details</span>
                            </div>
                            <div class="divider-risk"></div>
                            <div class="risk-content">
                                <div class="risk-details">
                                    <p><strong>Risk Category:</strong> High</p>
                                    <p><strong>Explanation:</strong></p>
                                    <ul>
                                        <li>The driver’s age is {st.session_state.user_data.get('age', 'Age not provided')}, which aligns with Rule 1 and Rule 2, classifying it as a high-risk factor.</li>
                                        <li>With the vehicle being a {st.session_state.user_data.get('model_year', 'Name not provided')} model, it meets the conditions of Rule 3, indicating a high-risk category.</li>
                                        <li>The total claims fall within {st.session_state.user_data.get('total_claims', 'Claims not provided')}, which qualifies as a high-risk factor according to Rule 6.</li>
                                        <li>The odometer reading lies between {st.session_state.user_data.get('odoo_range', 'Range not provided')}, marking it as a moderate level of usage.</li>
                                        <li>The city, {st.session_state.user_data.get('Address', 'Location not provided')}, is not associated with high traffic or criminal activity, making it a negligible risk factor under Rule 8.</li>
                                        <li>The vehicle's make is {st.session_state.user_data.get('make', 'Name not provided')}, which is categorized as expensive. Its model, {st.session_state.user_data.get('model', 'Name not provided')}, falls into the premium category, but the variant, Plus S, is relatively affordable. As a whole, the vehicle qualify as an expensive car per Rule 9.</li>
                                        <li>Considering all the rules, the overall risk is assessed to be High.</li>
                                    </ul>
                                    <p><strong> Based on the risk category High, premium amount $23.32</strong></p>
                                </div>
                            </div>
                            <div class="download-button">
                                <a href="data:application/pdf;base64,{pdf_base64}" download="quotation_{st.session_state.quotation_id}.pdf">
                                    <button>Download Auto Quote as PDF</button>
                                </a>
                            </div>
                        </div>
                    """,
                    unsafe_allow_html=True
                )
            elif fuel_type == 'Diesel': # If the vehicle is Diesel
                # Injecting custom CSS styles for quotation container
                st.markdown(
                    """
                    <style>
                    .custom-container {
                        height: 600px
                        width: 400px;
                        padding: 20px;
                        margin: 0 auto;
                        border: 2px solid #2969B7;
                        font-family: Arial, sans-serif;
                    }
                    .custom-container-risk {
                        border: 2px solid #2969B7;  /* Tomato color for a clear box */
                        padding: 15px;
                        background-color: #f9f9f9;
                        border-radius: 10px;
                        text-align: left;
                        margin-left: -123px;
                        width: 516px;
                        height: 555px; /* Set the desired height */
                        /* Add scrollbars if content overflows */
                    }
                    .risk-evaluation {
                        font-size: 18px;
                        font-weight: bold;
                        color: #2969B7;  /* Matching the border color */
                    }
                    .divider-risk {
                        height: 2px;
                        background-color: #2969B7;
                        margin-top: 10px;
                        margin-bottom: 15px;
                    }
                    .personal-details {
                        font-size: 18px;
                        font-weight: bold;
                        color: #2969B7; 
                    }
                    .vehicle-details {
                        font-size: 18px;
                        font-weight: bold;
                        color: #2969B7; 
                    }
                    .vehicle-image {
                        width: 35%;
                        margin-left: 200px;
                        margin-top: -250px
                    }
                    .deductible-details {
                        font-size: 18px;
                        font-weight: bold;
                        color: #2969B7; 
                    }
                    .quotation-id {
                        text-align: right;
                        width: 100%;
                        margin-top: -30px
                    }
                    .download-button {
                        margin-top: 10px;
                    }
                    # .hidden-content {
                    #     display: none;
                    # }
                    .show-more:checked + .hidden-content {
                        display: block;
                    }
                    .show-more-label {
                        color: black;
                        cursor: pointer;
                    }
                    .spinner-container {
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        margin-top: -20px;
                        margin-left: -800px;
                    }

                    .spinner {
                        animation: spin 3s linear forwards;
                    }

                    @keyframes spin {
                        0% {
                            transform: rotate(0deg);
                        }
                        100% {
                            transform: rotate(360deg);
                        }
                    }

                    .message {
                        font-size: 1rem;
                        color: #333;
                    }
                    .first-container {
                        margin-bottom: 20px;  
                    }
                    .custom-container-risk-evaluation {
                        border: 2px solid #2969B7;
                        padding: 15px;
                        background-color: #f9f9f9;
                        border-radius: 10px;
                        text-align: left;
                        margin-left: -123px;
                        width: 522px;
                        height: 684px;
                    }
                    
                    </style>
                    """, 
                    unsafe_allow_html=True
                )
                
                
                if 'image_file' in st.session_state:  # Check if an image file exists in session state
                    image_file = st.session_state.image_file  # Get the uploaded image file
                    base65_image = display_uploaded_imagenow(image_file)  # Convert image file to base64
                else:
                    base65_image = ""  # If no image uploaded, set it as empty

                current_date = datetime.now()  # Get current date and time
                day = current_date.day  # Get the day from current date
                year = current_date.year  # Get the year from current date
                month = current_date.month  # Get the month from current date
                st.session_state.quotation_id = f"AIG-{year}{month:02d}{day:02d}-001"  # Generate unique quotation ID
                vehicle_image_path = st.session_state["image_vehicle"]  # Get vehicle image path
                pdf = create_pdf(vehicle_image_path)  # Create the PDF with vehicle images
                pdf_output = f"quotation_{st.session_state.quotation_id}.pdf"  # Define the output PDF file name
                pdf.output(pdf_output)  # Save the generated PDF
                with open(pdf_output, "rb") as pdf_file:  # Open the PDF in binary mode
                    pdf_base64 = base64.b64encode(pdf_file.read()).decode('utf-8')  # Convert PDF to base64 format
                # Injecting custom CSS styles for quotation container

                st.markdown(
                    f"""
                    <div class="custom-container-risk first-container">
                        <div class="personal-details">
                            <span>Personal Details(Policy Holder)</span>
                        </div>
                        <div class="quotation-id">
                        <span><b>Auto Quote ID: {st.session_state.quotation_id}</b></span>
                        </div>
                        <div class="divider-risk"></div>
                        <div class="personal-content">
                            <p>{st.session_state.user_data.get('full_name', 'Name not provided')}, aged {st.session_state.user_data.get('age', 'Age not provided')} resides in {st.session_state.user_data.get('Address', 'State not selected')}. He purchased {st.session_state.user_data.get('make', 'Make not provided')} recently.</p>
                        </div>
                        <div class="vehicle-details">
                            <span>Vehicle Details</span>
                        </div>
                        <div class="divider-risk"></div>
                        <div class="vehicle-container">
                            <div class="vehicle-text">
                                <p><strong>Your driver’s license number:</strong> {st.session_state.user_data.get("license_no", 'Name not provided')}</p>
                                <p><strong>Your VIN number:</strong> {st.session_state.user_data.get("vin_number", 'Name not provided')}</p>
                                <p><strong>Make:</strong> {st.session_state.user_data.get('make', 'Name not provided')}</p>
                                <p><strong>Model:</strong> {st.session_state.user_data.get('model', 'Name not provided')}</p>
                                <p><strong>Year:</strong> {st.session_state.user_data.get('model_year', 'Name not provided')}</p>
                                <p><strong>Date of Purchase:</strong> {st.session_state.user_data.get('date', 'Name not provided')}</p>
                                <p><strong>Vehicle Type:</strong> {st.session_state.user_data.get('fuel_type', 'Fuel type not provided')}</p>
                                <p><strong>Primary Use:</strong> {st.session_state.user_data.get('primary_use', 'Primary use not provided')}</p>
                                <p><strong>Deductible Amount:</strong> {st.session_state.user_data.get('deductible_range', 'Primary use not provided')}</p>
                            </div>
                        </div>
                        <div class="vehicle-image">
                                <img src="data:image/png;base64,{base65_image}" alt="Vehicle Image" style="width: 100%;">
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if "show_premium_clicked" not in st.session_state:  # Check if the premium button clicked state is not in session state
                    st.session_state.show_premium_clicked = False  # Set default state for premium click

                if st.button("Show Premium Amount"):  # Show premium amount button
                    st.session_state.expander_open = True  # keep open previous expanders
                    st.session_state.show_premium_clicked = True  # Set the flag for premium clicked
                    st.rerun()  # Rerun the app to refresh and show premium details
                if st.session_state.show_premium_clicked:  # If premium clicked flag is set
                    message = st.chat_message("assistant").markdown("Please wait...")  # Show chat message while processing
                    col1, col2 = st.columns([1, 40])  # Create columns for the premium details
                    with col2:
                        with st.spinner("Processing..."):  # Show spinner while processing
                            time.sleep(3)  # Simulate processing delay
                        message.markdown("Done! Your Quote is ready")  # Display completion message
                    # Injecting custom CSS styles for quotation container
                    st.markdown(
                        f"""
                        <div class="custom-container-risk-evaluation">
                            <div class="hidden-content">
                                <div class="risk-evaluation">
                                    <span>Risk Evaluation Details</span>
                                </div>
                                <div class="divider-risk"></div>
                                <div class="risk-content">
                                    <div class="risk-details">
                                        <p><strong>Risk Category:</strong> High</p>
                                        <p><strong>Explanation:</strong></p>
                                        <ul>
                                            <li>The driver’s age is {st.session_state.user_data.get('age', 'Age not provided')}, which aligns with Rule 1 and Rule 2, classifying it as a low-risk factor.</li>
                                            <li>With the vehicle being a {st.session_state.user_data.get('model_year', 'Name not provided')} model, it meets the conditions of Rule 3, indicating a low-risk category.</li>
                                            <li>The total claims fall within {st.session_state.user_data.get('total_claims', 'Claims not provided')}, which qualifies as a high-risk factor according to Rule 6.</li>
                                            <li>The odometer reading lies between {st.session_state.user_data.get('odoo_range', 'Range not provided')}, marking it as a moderate level of usage.</li>
                                            <li>The city, {st.session_state.user_data.get('Address', 'Location not provided')}, is associated with high traffic and a history of criminal activity, making it a significant high-risk factor under Rule 8.</li>
                                            <li>The vehicle's make is {st.session_state.user_data.get('make', 'Name not provided')}, which is categorized as expensive. Its model, {st.session_state.user_data.get('model', 'Name not provided')}, falls into the premium category, and the variant, Plus S, is highly desirable, increasing the risk of theft or costly repairs. As a whole, the vehicle qualifies as a high-risk car per Rule 9.</li>
                                            <li>Considering all the rules, the overall risk is assessed to be High.</li>
                                        </ul>
                                        <p><strong>Based on the risk category High, premium amount $1916.00</strong></p>
                                    </div>
                                </div>
                                <div class="download-button">
                                    <a href="data:application/pdf;base64,{pdf_base64}" download="quotation_{st.session_state.quotation_id}.pdf">
                                        <button>Download Auto Quote as PDF</button>
                                    </a>
                                </div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
    user_input = st.chat_input("Type your message", key="chat_new") # displayed chatbox for the autoscrolling the quotation