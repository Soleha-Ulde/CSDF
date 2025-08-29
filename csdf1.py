from __future__ import print_function
from email import message_from_file
import os
import quopri
import base64

EML_PATH = r"C:\Users\Soleha Ulde\Downloads\Email Confirmation to Join Sinhgad Academy of Engineering.eml"

def process_payload(payload, eml_filename):
    print(payload.get_content_type() + "\n" + "=" * len(payload.get_content_type()))
    body = payload.get_payload(decode=True)
    if body is None:
        return
    if payload.get_charset():
        body = body.decode(payload.get_charset())
    else:
        try:
            body = body.decode()
        except UnicodeDecodeError:
            body = body.decode('cp1252')

    if payload.get_content_type() == "text/html":
        outfile = os.path.basename(eml_filename) + ".html"
        open(outfile, 'w').write(body)
    elif payload.get_content_type().startswith('application'):
        outfile = open(payload.get_filename(),'wb')
        body = base64.b64decode(payload.get_payload())
        outfile.write(body)
        outfile.close()
        print("Exported:  {}\n".format(outfile.name))
    else:
        print(body)


def main(input_file):
    emlfile = message_from_file(input_file)
    for key,value in emlfile._headers:
        print("{} : {}".format(key,value))

    print("\nBody\n")
    if emlfile.is_multipart():
        for part in emlfile.get_payload():
            process_payload(part,input_file.name)
        else:
            process_payload(emlfile, input_file.name)

if __name__ == '__main__':
    with open(EML_PATH,'r') as f:
        main(f)


