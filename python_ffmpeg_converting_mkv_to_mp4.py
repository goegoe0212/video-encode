import subprocess
import os

def convert_mkv_to_mp4(input_path, ffmpeg_path):
    # 出力ファイル名を.mkvから.mp4に変更
    file_name = os.path.basename(input_path.rsplit('.', 1)[0] + '.mp4')
    # 出力ファイルのパスを設定
    output_path = os.path.join('D:\動画エンコード\変換データ', file_name)

    # FFMPEGコマンドを構築
    command = [
        ffmpeg_path,
        '-i', input_path,
        '-codec', 'copy',  # ビデオとオーディオコーデックは変更しない
        output_path
    ]

    # FFMPEGコマンドを実行
    subprocess.run(command)
def main():
    # FFMPEG実行ファイルのパス
    ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg.exe')

    # ユーザーによるフォルダパスの入力
    folder_path = input("フォルダパスの入力: ")

    # 指定フォルダ内のすべての.mkvファイルを探索
    for file in os.listdir(folder_path):
        if file.endswith('.mkv'):
            file_path = os.path.join(folder_path, file)
            print(f"Converting {file_path} to MP4...")
            convert_mkv_to_mp4(file_path, ffmpeg_path)
            print(f"Finished converting {file_path}")

if __name__ == "__main__":
    main()
