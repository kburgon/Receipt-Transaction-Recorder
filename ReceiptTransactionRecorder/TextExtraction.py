""" Kevin Burgon -- 11/10/2016
    This is an implementation of text extraction for Google Cloud Vision, based off the
    sample provided by Google for labeling images.  I have adapted it for my own needs.

"""
import argparse
import base64

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


def extractText(photo_file):
    """Run text extraction on a single image."""

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)

    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'TEXT_DETECTION',
                }]
            }]
        })
        response = service_request.execute()
        imageText = response['responses'][0]['textAnnotations'][0]['description']
        return imageText

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    args = parser.parse_args()
    imageText = extractText(args.image_file)
    fout = open('results.txt', 'w')
    fout.write(imageText)
    fout.close()
