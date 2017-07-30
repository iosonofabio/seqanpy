#!/bin/bash
# only deploy builds for a release_<sematic-version>_RC?? tag to testpypi
if [ -z $TRAVIS_TAG ]; then
  echo 'No TRAVIS_TAG, exit'
  exit 0
fi
TAG1=$(echo $TRAVIS_TAG | cut -f1 -d_)
TAG2=$(echo $TRAVIS_TAG | cut -f2 -d_)
TAG3=$(echo $TRAVIS_TAG | cut -f3 -d_)
if [ -z $TAG2 ]; then
  echo 'No TAG2, exit'
  exit 0;
fi
if [ $TAG1 != 'release' ]; then
  echo 'Not a release tag, exit'
  exit 0;
fi

VERSIONSETUP=$(grep 'version=' setup.py | sed 's/^\s*version="\(.*\)",\s*$/\1/')
if [ $TAG2 != $VERSIONSETUP ]; then
  echo "Wrong version (TAG=$TAG2, setup.py=$VERSIONSETUP), exit"
  exit 0;
fi

if [ $TRAVIS_PYTHON_VERSION != '3.6' ]; then
  echo "Not python 3.6, exit"
  exit 0;
fi

# deploy onto pypitest unless you have no RC
if [ -z $TAG3 ]; then
  TWINE_PASSWORD=${TWINE_PASSWORD_PYPI}
  TWINE_REPOSITORY='https://upload.pypi.org/legacy/'
  echo 'Deploying to production pypi'
elif [ ${TAG3:0:2} == 'RC' ]; then
  TWINE_PASSWORD=${TWINE_PASSWORD_TESTPYPI}
  TWINE_REPOSITORY='https://test.pypi.org/legacy/'
  echo 'Deploying to testpypi'
else
  echo "Tag not recognized: $TRAVIS_TAG"
  exit 1
fi

# Build source dir
python setup.py sdist
echo "Contents of 'dist':"
ls dist

# TODO: rename file (Pyi hates same-naming)
if [ -z $TAG3 ]; then
  echo "Production version, no renaming"
  SDIST_FN=dist/seqanpy-"${TAG2}".tar.gz
else
  echo "Testing version, renaming..."
  SDIST_FN=dist/seqanpy-"${TAG2}_${TAG3}".tar.gz
  mv dist/seqanpy-"${TAG2}".tar.gz "${SDIST_FN}"
fi
echo "${SDIST_FN}"

# Install twine
pip --version
pip install twine

# Upload
twine upload --repository-url "${TWINE_REPOSITORY}" -u "${TWINE_USERNAME}" -p "${TWINE_PASSWORD}" "${SDIST_FN}"
