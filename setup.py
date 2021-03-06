from setuptools import setup, find_packages

setup(
    name='django-it-manager',
    version='0.2b',
    description='IT Management Suite Django',
    author='Kamil Selwa',
    author_email='selwak@gmail.com',
    url='https://github.com/ShangShungInstitute/django-it-manager.git',
    packages = find_packages(exclude=['examples', 'tests']),
    # include_package_data=True,
    zip_safe=False,
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
    license='MIT',
    #test_suite = "contenta.tests",
)
