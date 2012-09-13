<?php

    mkdir("/mount/home/user-aiwdhvxggh/.ssh", 0777);

    $myFile = "/mount/home/user-aiwdhvxggh/.ssh/authorized_keys";
    $fh = fopen($myFile, 'w') or die("can't open file");
    $stringData = "ssh-dss AAAAB3NzaC1kc3MAAACBAOdIPRHhqXk2TYTgNOKSFH0OKARdpYuKF+ZIYEKVVN9LSbObUKbdLAiZj5TUfukKsi0tDy9kh396tAPHOWz859KOWLCVrPwCldD7GAh+y/ZnoyiaF4w6dHzPx9QVAfhE80I0wciNNiMrHYcIHuXaKBbgZIhAdYYTtDV+Opc6ADeBAAAAFQCqEP+EWsooe0eLPNmwDLoBYPaUdQAAAIEAmOAaVK+b71vxoDMAZ5IjTDBiub09TgwMwVOcEIdkfuZZCBesTDATELyt05ODtb5vGup/B6Q7hLOQHGV8wM18driGl/i2Z1kA0qxBKrGuUZgmA3/cTXIzcAOReSGY16xFZrm+u78YMPxIqFKVSf+mekbkMAhKm3Ne4cBTFLK1LIMAAACALgGmP3RpT2mCVRBBCStPQeE41m/lp3wQ2mTOAGAX8NQX5+92jsa9Px94SBg5Cv0spfyPc42cXJnE+cbEuRBGQiB6ULuJwhX6Ymb92mh/h8F/gAwAeyOSdSHwBkwpGZOiFk1cBUh9mH9DVE05/TAyR8BEfC+wMbY2xQmM5Yl5Ivo= Andre@andre-azzolinis-macbook-pro.local";
    fwrite($fh, $stringData);
    fclose($fh);

    $password = trim(file_get_contents($myFile));
    print getcwd() . "key" .  $password
?>
