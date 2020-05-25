# Issue Summary 

For our web stack debugging project #3 we were given a server where there was a problem and we had to find out why Apache was returning error 500, and then fix it. At first we searched the server for the problem using the "strace" function. In the end we were able to find and fix the problem that caused error 500 to return. The problem was centered on the fact that there was an error in the wordpress configuration php file and it generated this error 500 return.

# Timeline

2:00 pm - The server is accessed to verify by curl, which returns the Apache.

2:20 pm - The error search begins by searching for the processes that were running at the time.

4:00 pm - An inconsistency was found in the wordpress configuration php file.

4:20 pm - The executable file begins to be generated to fix the problem in the wordpress configuration php file.

4:40 pm - Execute the file created to fix the problem in the wordpress configuration php file.

4:45 pm - You get the expected result of the curl request to the server and no longer generate error 500.

# Root cause and resolution

The problem was centered in that there was an error in the php file of configuration of wordpress and generated this return of error 500. When modifying the file of configuration it is necessary to be very rigorous in not committing any error since the simple fact to put badly a letter in an address of a file, generates problems and the server did not manage to find the file, generating an internal problem in the server and returning error 500.

This type of errors are very common in servers that contain wordpress since as the program plugins are installed, the configuration file is automatically configured, and if there is any problem during the update, the file must be modified manually or back to a previous edition of it.

By the "strace" command, you can find this kind of errors more easily because we focus specifically on the processes that are running and therefore, generating errors in the server, so we avoid wasting time looking at each file on the server and also avoid damaging other files that may be correct.

# Corrective and preventative measures

In the future it is necessary to be more careful when configuring wordpress files and always make a copy of the file before modifying it so that you can later compare them and know where the problem is. On the other hand it is very important to generate a solution so that when this type of problem happens, the client does not have this return error when accessing the web page, an example of a solution is to redirect to a backup server so that it can have access while it is being solved or modifications are made to the main server. 

It is important not to upload the updates directly to the server without being sure that everything is working correctly since it can generate this type of problems and leave the web page disabled for a long time. 

Finally, always keep in mind the execution processes that are running at the moment to be able to have control of the server and to be able to find problems in a faster way.