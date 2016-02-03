It's riak! and python!

You get the rapid development of python with a
highly scalable nosql backend!

spec built with pyp2rpm with minor editing:

- *Source0* changed to upstream github,using `%{version}` in URL for
  easy maintenance.

- *setup.py* imports it's version information from *PKG-INFO*;  this is
  included in the `pip` bundle
  but not committed to the upstream repo.  I got lazy and dropped it
  in with a heredoc; watch for that to go away in the changelog.

- No tests.  The full test suite attempts to make connections to a riak
  cluster, and I don't have a controlled environment set up for that.
  Watch for information about testing in the changelogs.

- Added some *BuildRequires* exposed with *%test* enabled, but commented
  them out for now.

- pyp2rpm gave me
  `%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info` and such
  in %files, and I'm not into that.  The `?` was replaced with
  `%{python2_version}` and such because
  one day, there might be a two digit subversion or a python4, and
  this way has no surprises.

- `%autosetup -qn`had the wrong path for the github tarball. meh.

COPR builds are happening at https://copr.fedorainfracloud.org/coprs/immanetize/python-riak/
