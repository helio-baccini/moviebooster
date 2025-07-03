@echo off
setlocal

:: Caminho temporário no diretório do usuário
set "PASTA_PROJETO=%USERPROFILE%\LocadoraFilmesTemp"
set "ORIGEM=%~dp0"

:: Cria a pasta temporária e copia tudo
if exist "%PASTA_PROJETO%" rmdir /s /q "%PASTA_PROJETO%"
mkdir "%PASTA_PROJETO%"
xcopy "%ORIGEM%*" "%PASTA_PROJETO%\" /E /I /Y

:: Iniciar o backend a partir da subpasta \backend
cd /d "%PASTA_PROJETO%\backend"
start "" cmd /k "python app.py"

:: Abrir o index.html da pasta frontend no navegador
start "" "%PASTA_PROJETO%\frontend\index.html"

:: Aguarda um tempo e pergunta se deseja apagar
timeout /t 10 >nul
set /p RESPOSTA="Deseja apagar a pasta temporária após execução? (s/n): "
if /i "%RESPOSTA%"=="s" (
    rmdir /s /q "%PASTA_PROJETO%"
    echo Pasta deletada.
) else (
    echo Pasta mantida em: %PASTA_PROJETO%
)

endlocal
pause
