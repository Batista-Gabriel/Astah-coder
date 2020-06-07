# What is this for?

Making a project with my college mates, i notticed that transforming "astah" into java was pretty boring. So why not automate?

It's a simple program that take a given astah screenprint and transforms it into a java code.


## Atention



**change "username" to Your username and "image" to your image name**

Here:

```python
ocr.pytesseract.tesseract_cmd = r"C:\Users\userName\AppData\Local\Tesseract-OCR\tesseract.exe"
```

And here

```python
return (ocr.image_to_string(Image.open(r'image.png'), lang='por'))
```

## You need 

*  Python

* To download [Pytesseract](https://github.com/tesseract-ocr/tesseract/wiki)
* Install pyteteseract and pillow - pip install pytesseract pillow

## Usage
Take a print and cut Like this then paste inside your python project post

<img src="https://i.imgur.com/pqtyT0t.png" width="200" height="212">

**Please make a class at a time and use the zoom so image may be easier to be read**

And the code will make this appear

```python
private Long  id;

private String  name ;

...

public User(){

}

public getld(){

}

public setld( Long id ){

}



...

public getUserCategory( Integer category ){

}
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
