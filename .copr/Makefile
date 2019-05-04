BUILDROOT:=$(shell [ -d "/build" ] && echo "/build" || echo ".")
TMPDIR:=$(shell mktemp -d)

srpm:
	yum copr enable -y managerforlustre/buildtools
	yum install -y python2-devel python2-setuptools_scm
	rm -rf ${TMPDIR}/_topdir
	rm -rf ${TMPDIR}/scratch
	mkdir -p ${TMPDIR}/_topdir/SOURCES
	mkdir -p ${TMPDIR}/scratch
	cp -r ${BUILDROOT}/iml_sos_plugin \
		${BUILDROOT}/LICENSE.txt \
		${BUILDROOT}/MANIFEST.in \
		${BUILDROOT}/README.md \
		${BUILDROOT}/requirements.txt \
		${BUILDROOT}/setup.py \
		${BUILDROOT}/python-iml_sos_plugin.spec ${TMPDIR}/scratch
	cd ${TMPDIR}/scratch && python setup.py sdist && cp ${TMPDIR}/scratch/dist/iml_sos_plugin*.tar.gz ${TMPDIR}/_topdir/SOURCES
	rpmbuild -bs --define "_topdir ${TMPDIR}/_topdir" ${TMPDIR}/scratch/python-iml_sos_plugin.spec
	cp -r ${TMPDIR}/_topdir/SRPMS/* $(outdir)
