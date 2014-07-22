'''
TODO:
    * Pass files by argument
    * Use fido for file verification
'''
import os
#import fido
# Map of quality per file type per category
file_quality = {'.txt': 95, '.csv': 100}

# List of files to parse
file_list = ['text.txt', 'data.csv']
# Storing qualities
files_quality = []
for file in file_list:
    fileName, fileExtension = os.path.splitext(file)
    files_quality.append(file_quality[fileExtension])
    print '[{}{}] preservation status: {}'.format(fileName,
                                                  fileExtension,
                                                  file_quality[fileExtension])


# Average quality of this submission
print files_quality
sum = 0
for quality in files_quality:
    sum += quality

print sum / len(files_quality)

#fido.main('text.txt')
