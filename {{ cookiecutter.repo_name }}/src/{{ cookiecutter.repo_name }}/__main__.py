import sys

if __name__ == '__main__':
    from {{ cookiecutter.repo_name }}.cli import main

    sys.exit(main())
