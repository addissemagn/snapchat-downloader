## Bugs 
- [x] 500 error submitted with '/#first' b/c router handling only '/'

## Features/enhancements
### Tier 1
- [x] Command line args parsing
- [ ] Setup and serve on a AWS EC2 instance
- [ ] Storage! Any way to store in user's browser/computer or create a file that initiates the download process? 

### Tier 2
- [ ] Add metadata to files
- [ ] Visual for download status i.e. 300/4000 
    - [x] Command line
    - [ ] On website
- [ ] Store download status
    - [x] Store download status for each media
    - [ ] Live update log with status i.e. .txt file
    - [ ] Allow resuming download if log exists
- [x] Store links before downloading; avoid duplicate downloads
- [ ] Different structures for downloads i.e. all in one folder vs folders for year/month
- [ ] Add date range selector
- [ ] Settings for what folders to delete i.e. uploads/, downloads/, zips/ ("uploads/" must already exist for file upload via web)

### Tier 3
- [ ] Make into python package
- [ ] Multi-threading for faster downloads
- [ ] Captcha
 
## Error handling
- [ ] If the file uploaded is not correct i.e. memories_history.json

## Tests/optimizations
- [ ] Write tests
- [ ] Test with large memories_history.json file
- [ ] Test downloading different media types
- [ ] Security i.e. email + leave as little (ideally zero) footprint of user data as possible
- [ ] Performance with muliple simultaneous downloads
