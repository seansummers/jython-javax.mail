#
# virtualenv -p /usr/local/bin/jython jython-env
# source ./jython-env/bin/activate
# pip install git+https://github.com/jiptool/jip@67cb2f58720fbe9522d76508dcad191e16d41be4
#
from jip.dist import setup

requires_java = {
    'dependencies':[
        ('com.sun.mail', 'javax.mail', '1.5.6'),
    ]
}

setup(
    requires_java=requires_java
)
