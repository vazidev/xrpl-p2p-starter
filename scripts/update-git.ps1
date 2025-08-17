param{$commitMsg, $branchName}
Write-Host 'Starting for commit with git add.'
git add .

Write-Host 'Commiting the changes with git commit'
git commit -m $commitMsg

Write-Host 'Pusshiing the changes to Github with git push'
git push origin $branchName

