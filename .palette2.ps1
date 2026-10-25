$root = (Get-Location).Path
$utf8 = New-Object System.Text.UTF8Encoding($false)

$map = [ordered]@{
  '#c9c2ff' = '#bfe8d8'; '#cfc7ff' = '#c9ede0'; '#b27ce0' = '#2f9e86'; '#c9c0e6' = '#c3ded5';
  '#ece8f8' = '#e9f3ee'; '#e6e1f2' = '#e2eee8'; '#e7e3fb' = '#e6f2ec'; '#eeeaf7' = '#eaf2ee';
  '#f0edf8' = '#ecf4ef'; '#efecf7' = '#ebf3ee'; '#f3eefb' = '#eef6f1'; '#f4f1fb' = '#f0f7f3';
  '#e9e5f4' = '#e7f0ea'; '#e9e5f2' = '#e7f0ea'; '#a9a5b6' = '#a0aca6'; '#b7b1c5' = '#aebbb4';
  '#bdb9c9' = '#b4c1ba'; '#cfc9dd' = '#c6d2cc'; '#dcd9e6' = '#d3ddd7'; '#e7e4ef' = '#e0e9e3';
  '#cfccd9' = '#c6d1cb'; '#d6d2df' = '#cdd8d2'; '#faf8ff' = '#f8fbf9'; '#faf9ff' = '#f8fbf9';
  '#fdfcff' = '#fbfdfb'; '#f7f6ff' = '#f8fbf9'; '#f7f6fb' = '#f6faf7'; '#f0edff' = '#e9f7f2';
  '#f4f4f7' = '#f2f6f3'; '#f3f1f9' = '#eff6f1'; '#ece9f5' = '#e8f0eb'; '#a49fb2' = '#97a49d';
  '#e9e5f4 ' = '#e7f0ea'; '#f0edf7' = '#ecf4ef'; '#e7e3f7' = '#e6f2ec'; '#f2f0f7' = '#eef5f0';
  '#eceaf3' = '#e8f0eb'; '#ddd0bf' = '#d5ddd7'; '#f2e7d8' = '#edf3ee'
}

$files = @(
  (Join-Path $root 'assets/css/pages.css'),
  (Join-Path $root 'assets/css/styles.css')
)

foreach ($file in $files) {
  $text = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)
  $before = $text
  foreach ($key in $map.Keys) {
    $text = [regex]::Replace($text, '(?i)' + [regex]::Escape($key.Trim()) + '\b', $map[$key])
  }
  $text = [regex]::Replace($text, '(?i)#0b0b12\b', '#06120f')
  $text = [regex]::Replace($text, '(?i)#2a2c3d\b', '#26332d')
  if ($text -ne $before) {
    [System.IO.File]::WriteAllText($file, $text, $utf8)
    Write-Output ("Updated: " + [System.IO.Path]::GetFileName($file))
  }
}
