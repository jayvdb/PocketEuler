# git checkout README.md
remark ./README.md > ./README.md.new
sed -i 's/&lt;/</g' README.md.new
sed -i 's:\\\\:\\:g' README.md.new
sed -i 's/&#x3A;/:/g' README.md.new
sed -i 's/\\\*\\\*/**/;s/\\\*\([^*]*\)$/*\1/g' README.md.new  # may need to guard against a star before the current star
sed -i 's/\\|/|/g' README.md.new
sed -i 's/\\_/_/g' README.md.new
sed -i 's/\\\[/[/g' README.md.new
# mv README.md.new README.md
# git diff README.md
