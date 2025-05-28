git checkout release-candidate
git merge main --allow-unrelated-histories
git push
git checkout dev
git merge main --allow-unrelated-histories
git push
