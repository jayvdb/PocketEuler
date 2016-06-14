git checkout lint-v5
git branch -m lint-v5-old
git checkout master
git checkout -b lint-v5

git merge --no-ff issue_3

git merge --no-ff misc-rendering-errors-v5  (this also has a conflict with bullet-nbsp)

git merge --no-ff bullet-nbsp-v5

git merge --no-ff issue_39-v5-a1

git merge --no-ff lint-v5-part1

git merge --no-ff bullet-nbsp-cherry-on-top

git merge --no-ff fix-unintended-italics (conflict with lint-fixes-misc-v5 to be fixed )


----


# git merge --no-ff different-hanging-indent
git merge --no-ff different-bullet

git merge --no-ff lint-fixes-misc-v5

git merge --no-ff lint-logic-goal


