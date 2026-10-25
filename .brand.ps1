$root = (Get-Location).Path
$utf8 = New-Object System.Text.UTF8Encoding($false)

$snippet = @'
        <a class="brand" href="__HREF__" aria-label="WebServicers __DASH__ home">
          <span class="brand-mark" aria-hidden="true">
            <svg viewBox="0 0 40 40" fill="none">
              <rect width="40" height="40" rx="12" fill="url(#wsMark)"/>
              <path d="M9.5 13.2 14.9 26.8 20 17.6 25.1 26.8 30.5 13.2" stroke="#fff" stroke-width="3.1" stroke-linecap="round" stroke-linejoin="round"/>
              <circle cx="33" cy="8.6" r="2.4" fill="#E4FF6A"/>
              <defs>
                <linearGradient id="wsMark" x1="4" y1="2" x2="36" y2="40" gradientUnits="userSpaceOnUse">
                  <stop stop-color="#17C79A"/>
                  <stop offset="1" stop-color="#086747"/>
                </linearGradient>
              </defs>
            </svg>
          </span>
          <span class="brand-text"><span class="brand-word">Web</span><span class="brand-word--accent">Servicers</span></span>
        </a>
'@

$files = Get-ChildItem -Path $root -Filter *.html -File
foreach ($file in $files) {
  $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
  $m = [regex]::Match($content, '(?s)<a class="brand" href="([^"]*)" aria-label="[^"]*">.*?</a>')
  if (-not $m.Success) {
    Write-Output ("SKIP: " + $file.Name)
    continue
  }
  $href = $m.Groups[1].Value
  $block = $snippet.Replace("__HREF__", $href).Replace("__DASH__", [string][char]0x2014).Trim()
  $updated = $content.Substring(0, $m.Index) + $block + $content.Substring($m.Index + $m.Length)
  [System.IO.File]::WriteAllText($file.FullName, $updated, $utf8)
  Write-Output ("Brand updated: " + $file.Name)
}
