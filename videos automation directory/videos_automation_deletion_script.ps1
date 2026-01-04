# Folder containing videos
$videoFolder = "C:\Users\syed abdullah\Downloads\Workspace II\january\recordings"

# Number of days
$daysOld = 30

# Video file extensions to target
$extensions = @("*.mp4", "*.mkv", "*.avi", "*.mov", "*.wmv")

# Calculate cutoff date
$cutoffDate = (Get-Date).AddDays(-$daysOld)

# Get and delete old video files
Get-ChildItem -Path $videoFolder -Include $extensions -Recurse -File |
Where-Object { $_.LastWriteTime -lt $cutoffDate } |
Remove-Item -Force
