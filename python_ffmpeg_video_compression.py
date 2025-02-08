import subprocess
import os

def compress_video(input_path, ffmpeg_path):
    # ファイル名と拡張子を取得
    file_name = os.path.basename(input_path)

    # 出力ファイルのパスを設定
    output_path = os.path.join('D:\動画エンコード\変換データ', file_name)

    # FFMPEGコマンドを構築
    command = [
        ffmpeg_path,  # FFMPEGのパスを使用
        '-i', input_path,
        '-c:v', 'h264_nvenc',  # NVIDIA GPUを使用するエンコーダー
        '-preset', 'p7',  # エンコード品質と速度のバランスを設定
        '-b:v', '1M',  # ビットレートを5Mbpsに設定
        '-c:a', 'copy',  # オーディオは変更しない
        output_path
    ]

    # FFMPEGコマンドを実行
    subprocess.run(command)

def main():
    # FFMPEG実行ファイルのパス
    ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg.exe')

    # ユーザーによるフォルダパスの入力
    folder_path = input("フォルダパスの入力: ")

    if not folder_path:
        folder_path = "D:\動画エンコード\元データ"      # 指定フォルダ内のすべての.mp4ファイルを探索
    for file in os.listdir(folder_path):
        if file.endswith('.mp4'):
            file_path = os.path.join(folder_path, file)
            print(f"Compressing {file_path}...")
            compress_video(file_path, ffmpeg_path)
            print(f"Finished compressing {file_path}")

if __name__ == "__main__":
    main()
