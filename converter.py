import sys

# this a method that converts from FASTQ to FASTA
# conversion happens by replacing '@' with '>' and removing the last two lines

def fromFASTQtoFASTA():
    # create output file
    outputFASTA = open('four_reads.fasta', 'w')
    # read input file
    with open('four_reads.fastq', 'r') as input_fastq:
        # readLines reads the file line based and puts them in a list 
        inputLines = input_fastq.readlines()
        for i in range(len(inputLines)):
            trimmedSeqLine = inputLines[i].strip()
        
            # conversion
            if '@' in trimmedSeqLine:
                trimmedSeqLine = trimmedSeqLine.replace('@', '>')
            elif trimmedSeqLine == '+' or inputLines[i-1].strip() =='+':
                continue

            # write to file
            outputFASTA.write(trimmedSeqLine+'\n')
            

fromFASTQtoFASTA()
        