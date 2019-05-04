BUILDROOT:=$(shell [ -d "/build" ] && echo "/build" || echo ".")
TMPDIR:=$(shell mktemp -d)

  srpm:
	yum install -y epel-release
	yum install -y rpm-build python2-devel python-setuptools
	yum install -y ${BUILDROOT}/deps/python2-setuptools_scm-1.15.7-2.el7.noarch.rpm
	rm -rf ${TMPDIR}/_topdir
	rm -rf ${TMPDIR}/scratch
	mkdir -p ${TMPDIR}/_topdir/SOURCES
	mkdir -p ${TMPDIR}/scratch
	cp -r ${BUILDROOT}/iml_sos_plugin ${BUILDROOT}/LICENSE.txt ${BUILDROOT}/MANIFEST.in ${BUILDROOT}/README.md ${BUILDROOT}/requirements.txt ${BUILDROOT}/setup.py ${BUILDROOT}/python-iml_sos_plugin.spec ${TMPDIR}/scratch
	cd ${TMPDIR}/scratch && python setup.py sdist && cp ${TMPDIR}/scratch/dist/iml_sos_plugin*.tar.gz ${TMPDIR}/_topdir/SOURCES
	rpmbuild -bs --define "_topdir ${TMPDIR}/_topdir" ${BUILDROOT}/python-iml_sos_plugin.spec
	cp -r ${TMPDIR}/_topdir/SRPMS/* $(outdir) 