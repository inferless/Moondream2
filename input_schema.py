INPUT_SCHEMA = {
    "image_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://github.com/rbgo404/Files/raw/main/moondream.jpg"]
    },
    "question":  {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["Describe this image."]
    }
}
