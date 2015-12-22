# rpm-opt-hooks

This package add hooks into RPM's automatic dependency generator to add a
opt(path) prefix to a package's provides and requires as needed.  It currently
makes the following assumptions:

* Packages install into a prefix of /opt/a[/b[/c]]
* If a library dependency can be found in /opt, the package will use it.  This
  is generally safe if you are building into a clean buildroot.

The prefix used will be "opt(a[/b[/c]])".  If you are using a module hierarchy
type naming scheme, the a, b, c names will correspond to the modules needed
to be loaded for the depedency to be resolved.

I think this approach could be made faily generic and useful for other similar
packages like SCLs.

## Usage

Simplest is to add it to your buildroot.  For example, in you mock config:

     config_opts['chroot_setup_cmd'] = 'install @buildsys-build rpm-opt-hooks'

Alternatively, packages using it can add it to their BuildRequires.

## Internals

It adds the opt.attr and optlibsymlink.attr files into /usr/lib/rpm/attrs.
These configure rpm to use its own scripts to process the provides and requires
for any files in /opt.  One key aspect of this is that it will disable the
default scripts for any files in /opt by setting %__elf_exclude_path and 
%__libsymlink_exclude_path.  NOTE: This will conflict with any other attempt
to override these by a similar package like Fedora's rpm-mpi-hooks.

The opt.prov and opt.req scripts will then perform the needed manipulation.
The opt.common file contains a common getoptname() function that can be
changed to handle different prefix naming schemes.

## History

This work is derived from rpm-mpi-hooks in Fedora by Sando Mani for handling
multiple MPI implementations.
