import os

test = open("pytest.tex","w")
test.write("\section{SOY UNA PRUEBA EN pytHON}")
test.close()
os.system("pdflatex test.tex")
