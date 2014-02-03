Attribute-Based Encryption for Expressing Client Privacy Options

Accessible at privatebook.herokuapp.com

Prototype: Social networking site with page profiles, options to upload info and status updates, and clients select specific sharing/privacy options. 
-	Collect and encrypt data with public keys with Javascript on page
-	Send AJAX request and send encrypted data to server
-	Use decryption key to decrypt data through PHP on server
-	Display to console the Attribute List with the client’s chosen options
-	Save decrypted data to database and create page for user

Privacy Options:
-	Who can see information: Advertisers/Service/No one
-	How long updates are shown: Month/Week/Day/Hour
-	Deleted info longevity: Forever/Never
-	Can use data for: Targeted Ads/Statistics/Partners/Nothing
-	Track Usage: Yes/No
-	GPS location: Yes/No

1st Phase:

1.	Create simple form for signups - privacy policy and give ID#
2.	Have a page for displaying profile info
3.	Database for storing personal information - privacy policy
4.	Client request for posting status or photo
5.  Server updates stream of posts on user personal page 

2nd Phase:

1.	Implement proper encryption scheme with encryption/decryption
2.	Store encrypted privacy data in database on creation
4.	Server must decrypt (showing user policy) to retrieve requested data
5.	Serve client requests after policy is presented to server

