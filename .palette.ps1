$root = (Get-Location).Path
$utf8 = New-Object System.Text.UTF8Encoding($false)

$hexMap = [ordered]@{
  '#2f4bff' = '#0b7a53'; '#1c32d6' = '#075c3f'; '#5b7bff' = '#17c79a'; '#3a5bff' = '#17c79a';
  '#1b2ed1' = '#086747'; '#6c4bff' = '#0e8c7a'; '#5636e9' = '#0a6a5f'; '#7c3aed' = '#0d5a5a';
  '#a855f7' = '#1aa585'; '#6228d7' = '#0a6b5c'; '#5233d6' = '#0a6b5c'; '#2a1a80' = '#064a40';
  '#2338cc' = '#086b49'; '#13217a' = '#063a2a'; '#3c2f80' = '#0a4a3c'; '#9a88ff' = '#5fc9ae';
  '#8f7bff' = '#4fbfa2'; '#7aa7ff' = '#5fbfa6'; '#8ca2ff' = '#7fdcc0'; '#b9c6ff' = '#b7e8d6';
  '#ff7a59' = '#ff8a5b'; '#d8f35c' = '#e4ff6a'; '#e6ff7a' = '#f0ff9c';
  '#fff6ec' = '#fff7ec'; '#fff6e6' = '#fff8ee';
  '#f4f2ff' = '#eef8f2'; '#f6f6fa' = '#f4f7f5'; '#e8e6f0' = '#e3eae5';
  '#0a0916' = '#081512'; '#14122a' = '#10231d'; '#5c5a70' = '#52605a'; '#8a87a0' = '#7f8c86';
  '#100d26' = '#04100d'; '#171238' = '#08211b'; '#241a5e' = '#0b3027'; '#2f2278' = '#104237';
  '#0b0a18' = '#06120f'; '#171331' = '#0b241d'; '#0d0b1f' = '#06120e'; '#0e0c18' = '#06120f';
  '#08070f' = '#040e0b'; '#221b4d' = '#0b241d'; '#2b2165' = '#0e332a'; '#241a52' = '#0b2b22';
  '#1c1640' = '#082018'; '#1b1740' = '#082018'; '#1b1530' = '#0b241d'; '#15112f' = '#082019';
  '#211a35' = '#0b241d';
  '#f5f6fa' = '#f4f7f5'; '#666a79' = '#55625c'; '#606574' = '#55625c'; '#4c5163' = '#3c4a44';
  '#e6e8ef' = '#e3eae5'; '#6b7182' = '#697871'; '#ebedf2' = '#e3eae5'; '#626775' = '#55625c';
  '#616675' = '#55625c';
  '#f2f1f8' = '#edf5f0'; '#f4f2f9' = '#f0f7f3'; '#f1f0f8' = '#edf5f0'; '#f1f1f5' = '#eff5f1';
  '#f1edff' = '#e9f7f2'; '#f0eef7' = '#eaf2ed'; '#efedf6' = '#e8f0eb'; '#eeecf6' = '#e8f0eb';
  '#eeecf5' = '#e6eee9'; '#eeefff' = '#ebf7f1'; '#eef1ff' = '#eaf7f0'; '#e9f1ff' = '#e9f6f0';
  '#f4f4ff' = '#f0f8f3'; '#fbfbfe' = '#fbfdfb'; '#f3f2f9' = '#f0f6f2'; '#eae7f2' = '#e3ebe6';
  '#ece9f4' = '#e6eee9'; '#ddd8f7' = '#d6e9df'; '#d8d5e4' = '#d3ded8'; '#c8c3d8' = '#c3d1ca';
  '#bcb7c9' = '#b6c4bd'; '#e9def5' = '#dff1e9'; '#e7f6ff' = '#e8f7f3'; '#e7f1fb' = '#e8f4f0';
  '#64607a' = '#5a6760'; '#4a475c' = '#45514b'; '#46435a' = '#414e48'; '#3b3a4d' = '#34413b';
  '#2a2738' = '#1f2b26'; '#2a2638' = '#1f2b26'; '#2a2635' = '#1f2b26'; '#232135' = '#1b2722';
  '#6b6678' = '#5f6b65'; '#5f5a72' = '#55625c'; '#55516a' = '#4f5b55'; '#4d4666' = '#47544e';
  '#4d4a5e' = '#45524c'; '#4d4960' = '#45524c'; '#4c4960' = '#45524c'; '#8b84a3' = '#7f948b';
  '#9a83c4' = '#86a89c'; '#8b8799' = '#7c8a83'; '#8a8798' = '#7c8a83'; '#7a7488' = '#6e7b74';
  '#9691a4' = '#8a968f'; '#716c80' = '#647169'; '#6f6a7e' = '#647169'; '#8a90a2' = '#7f8b84';
  '#c7ccda' = '#c2d0c8'; '#dfe4f5' = '#dbe8e1'; '#d9e0ff' = '#d7efe4'; '#14161f' = '#0b1f18';
  '#101323' = '#081a13'; '#a0a5b4' = '#93a198'; '#fbfaff' = '#fbfdfb'; '#f0eef6' = '#e9f1ec';
  '#f4f3f8' = '#f1f6f2'; '#eef0f6' = '#ebf2ee'; '#eef0f7' = '#ebf2ee'; '#8b8699' = '#7d8a83';
  '#9a95a8' = '#8b978f'; '#7a7588' = '#6e7b74'; '#c9cee4' = '#c2d0c8'
}

$targets = @()
$targets += Get-ChildItem -Path (Join-Path $root 'assets/css') -Filter *.css -File
$targets += Get-ChildItem -Path (Join-Path $root 'assets/img') -Filter *.svg -File
$targets += Get-ChildItem -Path $root -Filter *.html -File

foreach ($file in $targets) {
  $text = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
  $before = $text

  foreach ($key in $hexMap.Keys) {
    $pattern = '(?i)' + [regex]::Escape($key) + '\b'
    $text = [regex]::Replace($text, $pattern, $hexMap[$key])
  }

  $rgbaMap = [ordered]@{
    '20,\s*15,\s*60' = '8, 40, 30';
    '216,\s*243,\s*92' = '228, 255, 106';
    '10,\s*9,\s*22' = '8, 21, 18';
    '47,\s*75,\s*255' = '11, 122, 83';
    '255,\s*122,\s*89' = '255, 138, 91';
    '10,\s*8,\s*40' = '4, 24, 19';
    '108,\s*75,\s*255' = '14, 140, 122';
    '8,\s*5,\s*32' = '4, 20, 16';
    '4,\s*2,\s*20' = '3, 14, 11';
    '8,\s*5,\s*25' = '4, 20, 16';
    '30,\s*20,\s*60' = '6, 32, 25';
    '3,\s*2,\s*15' = '2, 12, 9';
    '10,\s*8,\s*30' = '4, 24, 19'
  }
  foreach ($key in $rgbaMap.Keys) {
    $pattern = 'rgba\(\s*' + $key + '\s*,'
    $text = [regex]::Replace($text, $pattern, 'rgba(' + $rgbaMap[$key] + ',')
  }

  if ($text -ne $before) {
    [System.IO.File]::WriteAllText($file.FullName, $text, $utf8)
    Write-Output ("Updated: " + $file.Name)
  }
}
