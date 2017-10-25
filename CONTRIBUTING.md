# Contributing

### Setup
1. Fork the repo.

2. Clone your repo to your PC.

3. Add the upstream as a remote. 
    
    `git remote add upstream https://github.com/condnsdmatters/intro_to_dl_group.git`

### Pushing Changes

1. Do your work on a development branch.
   ```
      git branch my_branch # if you start on master
      git checkout my_branch
      # do work 
      git add -s my-filesA my-filesB
      git commit -m "my commit message"
   ```

2. Update your master with other people's changes. 
   ```
       git checkout master
       git pull upstream master 
   ```

3. Add these changes to your development branch.
   ```
      git checkout my_branch
      git rebase master
   ```

4. Push your branch to your GitHub.
   ```
       git push origin my_branch
   ```

5. Open a pull request on Github (the website) to merge into master.

6. (Once accepted) Update your master again. See step 2.
