# video-encode

このリポジトリは、FFmpegを使用して動画をエンコードおよび圧縮するためのPythonスクリプトを含んでいます。
Nvidia GPU（h264_nvenc）を利用するため高速にエンコードできます。


## 必要条件

- [FFmpeg](https://www.ffmpeg.org/download.html) がインストールされていること
- Python 3.x
- 仮想環境 (venv)

## セットアップ

1. 仮想環境を作成します。

    ```sh
    python -m venv venv
    ```

2. 仮想環境をアクティブにします。

    - Windows:

        ```sh
        .\venv\Scripts\activate
        ```

    - Linux:

        ```sh
        source venv/bin/activate
        ```

## 使用方法

### MKVからMP4への変換

```sh
python python_ffmpeg_converting_mkv_to_mp4.py
```

### MP4映像の圧縮

```sh
python python_ffmpeg_converting_mkv_to_mp4.py
```