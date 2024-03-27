INPUT_SCHEMA = {
    "image_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://file-examples.com/storage/fe1b802e1565fe057a1d758/2017/10/file_example_JPG_100kB.jpg"]
    },
    "question":  {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["Describe this image."]
    }
}
