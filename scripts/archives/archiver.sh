#!/bin/sh

MAINFONT_ROOT_DIR="fonts"
CJK_ROOT_DIR="cjk-fonts"

# Change to root directory
cd ../..

# Build zip and tar.xz file archive of main gallery fonts
zip -r -9 scripts/archives/codeface-fonts $MAINFONT_ROOT_DIR --exclude \*.DS_Store
tar c --exclude=.DS_Store --exclude=./.DS_Store --exclude=./*/.DS_Store $MAINFONT_ROOT_DIR | xz --extreme -9 --force > "scripts/archives/codeface-fonts.tar.xz"

# Build zip and tar.xz file archive of CJK gallery fonts
zip -r -9 scripts/archives/codeface-cjk-fonts $CJK_ROOT_DIR --exclude \*.DS_Store
tar c --exclude=.DS_Store --exclude=./.DS_Store --exclude=./*/.DS_Store $CJK_ROOT_DIR | xz --extreme -9 --force > "scripts/archives/codeface-cjk-fonts.tar.xz"
