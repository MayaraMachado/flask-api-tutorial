# Flask Restful API

## Blog Posts - More Information About This Repo

You can find more information about this project/repository and how to use it in following blog post:

- to do

## Quick Start
To use this repository as starter for your project you can run these commands:

```shell
$ mkvirtualenv venv
$ pip install -r requirements.txt

```

## Running

### Using Python Interpreter
```shell
$ python wsgi.py
```

### Using Docker

TO DO


## Testing

Test are ran every time you build _dev_ or _prod_ image. You can also run tests using:

```console
~ $ pytest
```

## Pushing to GitHub Package Registry

```console
~ $ docker login docker.pkg.github.com --username MartinHeinz
Password: ...
...
Login Succeeded
~ $ make push VERSION=0.0.5
```

## Cleaning

Clean _Pytest_ and coverage cache/files:

```console
$ rm -rf .pytest_cache .coverage .pytest_cache coverage.xml
```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Mayara Machado - [@mchdax](https://twitter.com/mchdax)

Project Post: [https://mayaramachado.dev/](https://mayaramachado.dev/)

