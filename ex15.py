from sys import argv #import argv from system module

script, filename = argv #unpack argv into variables

txt = open(filename)	#open file and place file in var txt

print "Here's your file %r:" % filename #print file name
print txt.read() #Run read function on file object

print "Type the filename again:"
file_again = raw_input(">") #do it again but from within the script

txt_again = open(file_again) #new file object

print txt_again.read() #run read on new file object
txt.close()		#close file object
txt_again.close()	#close file object
