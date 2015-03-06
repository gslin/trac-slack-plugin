from setuptools import setup

setup(
    name='SlackNotifcationPlugin',
    version='0.1',
    description='Plugin to announce Trac changes in Slack',
    author='Wagner Pinheiro',
    url='https://github.com/wagnerpinheiro/trac-slack-plugin',
    license='BSD',
    packages=['slack_notification'],
    classifiers=[
        'Framework :: Trac',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'trac.plugins': 'slack_notification = slack_notification'
    }
)
