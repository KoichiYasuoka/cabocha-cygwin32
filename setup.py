import setuptools
import glob
import platform
if platform.system().startswith("CYGWIN") and platform.machine()!="x86_64":
  pass
else:
  raise OSError("cabocha-cygwin32 only for 32-bit Cygwin")

setuptools.setup(
  name="cabocha-cygwin32",
  version="0.2",
  packages=setuptools.find_packages(),
  data_files=[
    ("local/bin",glob.glob("bin/*")),
    ("local/libexec/cabocha",glob.glob("libexec/cabocha/*")),
    ("local/lib",glob.glob("lib/*.*")),
    ("local/etc",glob.glob("etc/*")),
    ("local/include",glob.glob("include/*")),
    ("local/share/man/man1",glob.glob("share/man/man1/*")),
    ("local/lib/cabocha/model",glob.glob("lib/cabocha/model/*"))
  ],
  install_requires=["mecab-cygwin32@git+https://github.com/KoichiYasuoka/mecab-cygwin32"]
)
