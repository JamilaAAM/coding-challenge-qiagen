## Coding# Coding challenge - QIAGEN

### Converter from FASTQ to FASTA
This application converts sequences from FASTQ to FASTA and inserts the output in a file called `four_reads.fasta`.  

In order to run the application you need to have python installed and then run the following command:

```sh
python converter.py
```

If you do not have python installed a Dockerfile is attached in which you only need to run the following two command lines from the root of the folder:

```sh
docker build -t coding-challenge .
docker run -v $(pwd):/challenge coding-challenge
```
