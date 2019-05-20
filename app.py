
#!/usr/bin/python

from flask import Flask, request, make_response, jsonify
import requests

app = Flask(__name__)

# *****************************
# Course Data
# *****************************
CourseNames = {

'certified business analysis professional preparatory course':'Certified Business Analysis Professional Preparatory Course',
'certified scrum product owner':'Certified Scrum Product Owner',
'citrep+':'CITREP+',
'enterprise architecture practicum - aop':'Enterprise Architecture Practicum - AOP',
'lean it foundation certification':'Lean IT Foundation Certification',
'ccsp cbk training seminar':'CCSP CBK Training Seminar',
'cissp cbk training seminar':'CISSP CBK Training Seminar',
'csslp cbk training seminar':'CSSLP CBK Training Seminar',
'advanced customer analytics':'Advanced Customer Analytics',
'agile testing':'Agile Testing',
'aisp qualified information security professional course':'AISP Qualified Information Security Professional Course',
'architecting iot solutions':'Architecting IoT Solutions',
'architecting software solutions':'Architecting Software Solutions',
'big data engineering for analytics':'Big Data Engineering for Analytics',
'business agility bootcamp':'Business Agility Bootcamp',
'business analysis for agile practitioners':'Business Analysis for Agile Practitioners',
'business process reengineering':'Business Process Reengineering',
'campaign analytics':'Campaign Analytics',
'certified enterprise architecture practitioner course':'Certified Enterprise Architecture Practitioner Course',
'certified less practitioner - principles to practices':'Certified LeSS Practitioner - Principles to Practices',
'certified scrummaster':'Certified ScrumMaster',
'client side foundation':'Client Side Foundation',
'cloud native solution design':'Cloud Native Solution Design',
'cobit 5 foundation':'COBIT 5 Foundation',
'communicating and managing change':'Communicating and Managing Change',
'containers for deploying and scaling apps':'Containers for Deploying and Scaling Apps',
'customer analytics':'Customer Analytics',
'cyber security for ict professionals':'Cyber Security for ICT Professionals',
'cybersecurity risk awareness':'Cybersecurity Risk Awareness',
'data analytics process and best practice':'Data Analytics Process and Best Practice',
'data and feature engineering for machine learning':'Data and Feature Engineering for Machine Learning',
'data driven decision making':'Data Driven Decision Making',
'data governance & protection':'Data Governance & Protection',
'data storytelling':'Data Storytelling',
'design secure mobile architecture':'Design Secure Mobile Architecture',
'designing cloud-enabled':'Designing Cloud-enabled',
'designing intelligent edge computing':'Designing Intelligent Edge Computing',
'developing smart urban iot solutions':'Developing Smart Urban IoT Solutions',
'devops engineering and automation':'DevOps Engineering and Automation',
'devops foundation with bizops':'DevOps Foundation with BizOps',
'digital & social engagement strategy':'Digital & Social Engagement Strategy',
'digital product strategy':'Digital Product Strategy',
'digital transformation planning':'Digital Transformation Planning',
'digital user experience design':'Digital User Experience Design',
'enterprise architecture masterclass':'Enterprise Architecture Masterclass',
'enterprise architecture practicum':'Enterprise Architecture Practicum',
'enterprise digital governance':'Enterprise Digital Governance',
'envisioning smart urban iot solutions':'Envisioning Smart Urban IoT Solutions',
'essential practices for agile teams':'Essential Practices for Agile Teams',
'feature engineering and analytics using iot data':'Feature Engineering and Analytics using IOT Data',
'feature extraction and supervised modeling with deep learning':'Feature Extraction and Supervised Modeling with Deep Learning',
'health analytics':'Health Analytics',
'humanizing smart systems':'Humanizing Smart Systems',
'innovation bootcamp':'Innovation Bootcamp',
'intelligent sensing and sense making':'Intelligent Sensing and Sense Making',
'introduction to blockchain & dlt for executives':'Introduction to Blockchain & DLT for Executives',
'continual service improvement certificate':'Continual Service Improvement Certificate',
'foundation certificate in it service management':'Foundation Certificate in IT Service Management',
'operational support and analysis certificate':'Operational Support and Analysis Certificate',
'release, control and validation certificate':'Release, Control and Validation Certificate',
'service offerings and agreements certificate':'Service Offerings and Agreements Certificate',
'machine reasoning':'Machine Reasoning',
'managing business analytics projects':'Managing Business Analytics Projects',
'managing cybersecurity risk':'Managing Cybersecurity Risk',
'mobile user experience design':'Mobile User Experience Design',
'new media and sentiment mining':'New Media and Sentiment Mining',
'object oriented analysis & design':'Object Oriented Analysis & Design',
'object oriented design patterns':'Object Oriented Design Patterns',
'pattern recognition and machine learning systems':'Pattern Recognition and Machine Learning Systems',
'persistence and analytics fundamentals':'Persistence and Analytics Fundamentals',
'platform engineering':'Platform Engineering',
'pmi agile certified practitioner':'PMI Agile Certified Practitioner',
'pmp for project managers':'PMP For Project Managers',
'portfolio, programme and project offices':'Portfolio, Programme and Project Offices',
'predictive analytics - insights of trends and irregularities':'Predictive Analytics - Insights of Trends and Irregularities',
'prince2':'PRINCE2',
'problem solving using pattern recognition':'Problem Solving using Pattern Recognition',
'product thinking for organisations':'Product Thinking for Organisations',
'python for data, ops and things':'Python for Data, Ops and Things',
'reasoning systems':'Reasoning Systems',
'recommender systems':'Recommender Systems',
'restful api design':'RESTful API Design',
'robotic systems':'Robotic Systems',
'secure software development lifecycle for agile':'Secure Software Development Lifecycle for Agile',
'securing iot':'Securing IoT',
'security notification and messaging fundamentals':'Security Notification and Messaging Fundamentals',
'sequence modeling with deep learning':'Sequence Modeling with Deep Learning',
'server side foundation':'Server Side Foundation',
'service design':'Service Design',
'social media analytics':'Social Media Analytics',
'spatial reasoning from sensor data':'Spatial Reasoning from Sensor Data',
'statistics bootcamp':'Statistics Bootcamp',
'statistics for business':'Statistics for Business',
'strategic business analysis':'Strategic Business Analysis',
'strategic design & innovation':'Strategic Design & Innovation',
'strategic futures & foresight':'Strategic Futures & Foresight',
'strategic product manager':'Strategic Product Manager',
'strategic product market fit':'Strategic Product Market Fit',
'supervised and unsupervised modeling with machine learning':'Supervised and Unsupervised Modeling with Machine Learning',
'systems thinking & root cause analysis':'Systems Thinking & Root Cause Analysis',
'technopreneurship':'Technopreneurship',
'text analytics':'Text Analytics',
'text processing using machine learning':'Text Processing using Machine Learning',
'vision systems':'Vision Systems',
'web analytics and seo':'Web Analytics and SEO',
'nus graduate diploma in systems analysis':'NUS Graduate Diploma in Systems Analysis',
'pmi agile certified practitioner ':'PMI Agile Certified Practitioner',
}

CourseLinks = {

'certified business analysis professional preparatory course':'https://www.iss.nus.edu.sg/executive-education/course/detail/certified-business-analysis-professional-(cbap)-preparatory-course',
'certified scrum product owner':'https://www.iss.nus.edu.sg/executive-education/course/detail/certified-scrum-product-owner-',
'citrep+':'https://www.iss.nus.edu.sg/executive-education/course/detail/certified-information-systems-security-professional--(cissp-exam-only)',
'enterprise architecture practicum - aop':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf---enterprise-architecture-practicum---aop-(sf)',
'lean it foundation certification':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf---lean-it-foundation-certification-(sf)',
'ccsp cbk training seminar':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--(isc)-ccsp-cbk-training-seminar-(sf)',
'cissp cbk training seminar':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--(isc)-cissp-cbk-training-seminar-(sf)',
'csslp cbk training seminar':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--(isc)-csslp-cbk-training-seminar-(sf)',
'advanced customer analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--advanced-customer-analytics-(sf)',
'agile testing':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--agile-testing-(sf)',
'aisp qualified information security professional course':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--aisp-qualified-information-security-professional-course-(sf)',
'architecting iot solutions':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--architecting-iot-solutions-(sf)',
'architecting software solutions':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--architecting-software-solutions-(sf)',
'big data engineering for analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--big-data-engineering-for-analytics-(sf)',
'business agility bootcamp':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf-business-agility-bootcamp',
'business analysis for agile practitioners':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--business-analysis-for-agile-practitioners-(sf)',
'business process reengineering':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--business-process-reengineering-(sf)',
'campaign analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf-campaign-analytics-(sf)',
'certified enterprise architecture practitioner course':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--certified-enterprise-architecture-practitioner-course-(sf)',
'certified less practitioner - principles to practices':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--certified-less-practitioner---principles-to-practices-(sf)',
'certified scrummaster':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--certified-scrummaster-(sf)',
'client side foundation':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--client-side-foundation-(sf)',
'cloud native solution design':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf---cloud-native-solution-design-(sf)',
'cobit 5 foundation':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--cobit-5-foundation-(sf)',
'communicating and managing change':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--communicating-and-managing-change-(sf)',
'containers for deploying and scaling apps':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--containers-for-deploying-and-scaling-apps-(sf)',
'customer analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--customer-analytics-(sf)',
'cyber security for ict professionals':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--cyber-security-for-ict-professionals-(sf)',
'cybersecurity risk awareness':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--cybersecurity-risk-awareness-(sf)',
'data analytics process and best practice':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--data-analytics-process-and-best-practice-(sf)',
'data and feature engineering for machine learning':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--data-and-feature-engineering-for-machine-learning--(sf)',
'data driven decision making':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--data-driven-decision-making-(sf)',
'data governance & protection':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--data-governance-protection-(sf)',
'data storytelling':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--data-storytelling-(sf)',
'design secure mobile architecture':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--design-secure-mobile-architecture-(sf)',
'designing cloud-enabled':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--designing-cloud-enabled-mobile-applications-(sf)',
'designing intelligent edge computing':'https://www.iss.nus.edu.sg/executive-education/course/detail/designing-intelligent-edge-computing-SF',
'developing smart urban iot solutions':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--developing-smart-urban-iot-solutions-(sf)',
'devops engineering and automation':'https://www.iss.nus.edu.sg/executive-education/course/detail/devops-engineering-and-automation-SF',
'devops foundation with bizops':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--devops-foundation-with-bizops-(sf)',
'digital & social engagement strategy':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--digital-social-engagement-strategy-(sf)',
'digital product strategy':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--digital-product-strategy-(sf)',
'digital transformation planning':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--digital-transformation-planning-(sf)',
'digital user experience design':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--digital-user-experience-design-(sf)',
'enterprise architecture masterclass':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--enterprise-architecture-masterclass-(sf)',
'enterprise architecture practicum':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--enterprise-architecture-practicum-(sf)',
'enterprise digital governance':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--enterprise-digital-governance-(sf)',
'envisioning smart urban iot solutions':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--envisioning-smart-urban-iot-solutions-(sf)',
'essential practices for agile teams':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--essential-practices-for-agile-teams-(sf)',
'feature engineering and analytics using iot data':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--feature-engineering-and-analytics-using-iot-data-(sf)',
'feature extraction and supervised modeling with deep learning':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--feature-extraction-and-supervised-modeling-with-deep-learning-(sf)',
'health analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--health-analytics_(sf)',
'humanizing smart systems':'https://www.iss.nus.edu.sg/executive-education/course/detail/humanizing-smart-systems-SF',
'innovation bootcamp':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--innovation-bootcamp-(sf)',
'intelligent sensing and sense making':'https://www.iss.nus.edu.sg/executive-education/course/detail/intelligent-sensing-and-sense-making',
'introduction to blockchain & dlt for executives':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--introduction-to-blockchain-dlt-for-executives-(sf)',
'continual service improvement certificate':'https://www.iss.nus.edu.sg/executive-education/course/detail/-nicf--itil%C3%A2-continual-service-improvement-certificate-(sf)',
'foundation certificate in it service management':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--itil-foundation-certificate-in-it-service-management-(sf)',
'operational support and analysis certificate':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--itil-operational-support-and-analysis-certificate-(sf)',
'release, control and validation certificate':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--itil-release-control-and-validation-certificate-(sf)',
'service offerings and agreements certificate':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--itil-service-offerings-and-agreements-certificate-(sf)',
'machine reasoning':'https://www.iss.nus.edu.sg/executive-education/course/detail/machine-reasoning',
'managing business analytics projects':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--managing-business-analytics-projects-(sf)',
'managing cybersecurity risk':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--managing-cybersecurity-risk-(sf)',
'mobile user experience design':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--mobile-user-experience-design-(sf)',
'new media and sentiment mining':'https://www.iss.nus.edu.sg/executive-education/course/detail/new-media-and-sentiment-mining-new',
'object oriented analysis & design':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--object-oriented-analysis-design-(sf)',
'object oriented design patterns':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--object-oriented-design-patterns-(sf)',
'pattern recognition and machine learning systems':'https://www.iss.nus.edu.sg/executive-education/course/detail/pattern-recognition-and-machine-learning-systems',
'persistence and analytics fundamentals':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--persistence-and-analytics-fundamentals-(sf)',
'platform engineering':'https://www.iss.nus.edu.sg/executive-education/course/detail/platform-engineering-SF',
'pmi agile certified practitioner':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--pmi-agile-certified-practitioner-(pmi-acp)-preparatory-course-acp-sf',
'pmp for project managers':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--pmp-for-project-managers-(sf)',
'portfolio, programme and project offices':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf-portfolio-programme-and-project-offices-(p3o)--foundation-practitioner',
'predictive analytics - insights of trends and irregularities':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--predictive-analytics---insights-of-trends-and-irregularities-(sf)',
'prince2':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--prince2-(projects-in-controlled-environments)---foundation-and-practitioner-certificate-(sf)',
'problem solving using pattern recognition':'https://www.iss.nus.edu.sg/executive-education/course/detail/problem-solving-using-pattern-recognition',
'product thinking for organisations':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--product-thinking-for-organisations-(sf)',
'python for data, ops and things':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--python-for-data-ops-and-things-(sf)',
'reasoning systems':'https://www.iss.nus.edu.sg/executive-education/course/detail/reasoning-systems',
'recommender systems':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--recommender-systems-(sf)',
'restful api design':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--restful-api-design-(sf)',
'robotic systems':'https://www.iss.nus.edu.sg/executive-education/course/detail/robotic-systems',
'secure software development lifecycle for agile':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--design-secure-mobile-architecture-ssdla-sf',
'securing iot':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--securing-iot-(sf)',
'security notification and messaging fundamentals':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--security-notification-and-messaging-fundamentals-(sf)',
'sequence modeling with deep learning':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--sequence-modeling-with-deep-learning-(sf)',
'server side foundation':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--server-side-foundation-(sf)',
'service design':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--service-design-(sf)',
'social media analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--social-media-analytics-(sf)',
'spatial reasoning from sensor data':'https://www.iss.nus.edu.sg/executive-education/course/detail/spatial-reasoning-from-sensor-data',
'statistics bootcamp':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--statistics-bootcamp-(sf)',
'statistics for business':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--statistics-for-business-(sf)',
'strategic business analysis':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--strategic-business-analysis-(sf)',
'strategic design & innovation':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--strategic-design-innovation-(sf)',
'strategic futures & foresight':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--strategic-futures-foresight-(sf)',
'strategic product manager':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--strategic-product-manager-(sf)',
'strategic product market fit':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--strategic-product-market-fit-(sf)',
'supervised and unsupervised modeling with machine learning':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--supervised-and-unsupervised-modeling-with-machine-learning-(sf)',
'systems thinking & root cause analysis':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--systems-thinking-root-cause-analysis-(sf)',
'technopreneurship':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--technopreneurship-(sf)',
'text analytics':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--text-analytics-(sf)',
'text processing using machine learning':'https://www.iss.nus.edu.sg/executive-education/course/detail/text-processing-using-machine-learning',
'vision systems':'https://www.iss.nus.edu.sg/executive-education/course/detail/vision-systems',
'web analytics and seo':'https://www.iss.nus.edu.sg/executive-education/course/detail/nicf--web-analytics-seo-(sf)',
'nus graduate diploma in systems analysis':'https://www.iss.nus.edu.sg/executive-education/course/detail/nus-graduate-diploma-in-systems-analysis-(sf)',
'pmi agile certified practitioner ':'https://www.iss.nus.edu.sg/executive-education/course/detail/pmi-agile-certified-practitioner--(pmi-acp-exam-only)',


}

# *****************************
# WEBHOOK MAIN ENDPOINT : START
# *****************************
@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent_name = req["queryResult"]["intent"]["displayName"]
    
    
    if intent_name == "GetCourseFees" : ##     
        respose_text = getCourseFeesIntent(req) ## Call your getWeatherIntentHandler with req object as input. 
        print(req) # to print the entire output for the request
    else:
        respose_text = "Im sorry, could you say that again?"
    # Branching ends here

    # Finally sending this response to Dialogflow.
    return make_response(jsonify({'fulfillmentText': respose_text}))

# ***************************
# WEBHOOK MAIN ENDPOINT : END
# ***************************


# *****************************
# Intent Handlers funcs : START
# *****************************

def getCourseFeesIntent(req):

    course = req.get("queryResult").get("parameters").get("Course")
    course = course.lower()

    if course in CourseLinks:
        
        CourseLinkOutput = CourseLinks[course]
        CourseNameOutput = CourseNames[course]
        
        return f"A typical ISS course cost between $200 - $4000. Many of the courses are heavily subsidised by the Singapore Government if you are a Citizen or Permanent Resident of Singapore. For a detailed breakdown of the course {CourseNameOutput}, please refer to the details in the following link. Thank you. {CourseLinkOutput}"
    
    else:
        return f"Please enter a course name to enquire. Thank you."

# ***************************
# Intent Handlers funcs : END
# ***************************


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)