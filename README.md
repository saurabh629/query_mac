**Note: This app is for Linux command line only.

This is simple python app to query MAC address and find the vendor details. The App will take the input from the user for the MAC Address. It will make REST API call to macaddress.io to find the vendor details and output vendor company, vendor address.

An APIkey is need to make a REST call. It is a pre-requisite to register to macaddress.io to get a personalised APIkey. The app will query the MAC address if its valid and return the output. In case of invalid MAC address error message is return. In case of HTTP error during the get request occurs, HTTP error is returned. If MAC addres does not below to any vendor then, message return is MAC address doe not below to registered block. 

The app contains single python file query_mac.py. It contains a requirement.txt file which includes all the dependencies of the python app. It contains a Dockerfile to create a docker image to run the app in a containerized fashion. Please follow the below steps to build and run the app.

0. Register to macaddress.io to get a personalized key 

1. Clone the repository to local directory
   
   git clone https://github.com/saurabh629/query_mac.git

2. cd to query_mac

3. Execute docker build command to create an image from the
   dockerfile
   
   docker build --tag query_mac:version1 .

4. Initiate the docker container
   
   docker run -it --name query-mac-app query_mac

5. Enter the MACaddress and APIKey input

6. Enter 'quit' to exit


