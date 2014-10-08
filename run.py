# 07/10/2014 HashTag Remover By Tom Peregrine & Charles Thomas
# Number: +442033895731
# Alternate Number: +44 20 3389 5713

from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def run():
    """Say a caller's name, and play an MP3 for them."""
    outputSentence = ""
    changes = 0
    
    returnMsg = ""
    
    word = str(request.values.get('Body', None))
    for letter in word:   
        if letter == "#":
            outputSentence += " "
            changes += 1
        else:
            outputSentence += letter
    
    returnMsg = str(changes) + """ change(s) were made
"""
    returnMsg += outputSentence
    
    #print returnMsg
    
    resp = twilio.twiml.Response()
    resp.message(returnMsg)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=3000)
