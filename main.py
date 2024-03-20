from pyscript import document
def run():
    htmlCode = input("Enter HTML code: ")
    cssCode = input("Enter CSS code: ")
    jsCode = input("Enter JavaScript code: ")
    output = input("Enter output: ")
    output.contentDocument.body.innerHTML = htmlCode + "<style>" + cssCode + "</style>"
    output.contentWindow.eval(jsCode)
