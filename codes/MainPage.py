import os
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QFileDialog

from PersonTracking import TrackerThread


class MainPage(QtWidgets.QMainWindow):
    """A class used to display the main page of the Person Tracking application."""

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        """Set up UI components."""

        self.setObjectName("Person Tracking")
        self.resize(1024, 615)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.navigate_bar = QtWidgets.QFrame(self.centralwidget)
        self.navigate_bar.setGeometry(QtCore.QRect(0, 0, 1024, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.navigate_bar.setFont(font)
        self.navigate_bar.setAutoFillBackground(True)
        self.navigate_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navigate_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navigate_bar.setObjectName("navigate_bar")

        self.title = QtWidgets.QLabel(self.navigate_bar)
        self.title.resize(770, 40)
        center_y = (self.navigate_bar.height() - self.title.height()) // 2
        self.title.setGeometry(QtCore.QRect(300, center_y, 770, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")

        self.side_bar1 = QtWidgets.QFrame(self.centralwidget)
        self.side_bar1.setGeometry(QtCore.QRect(744, 70, 280, 180))
        self.side_bar1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_bar1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_bar1.setObjectName("side_bar1")

        self.original_video_text = QtWidgets.QLabel(self.side_bar1)
        self.original_video_text.setGeometry(QtCore.QRect(10, 10, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.original_video_text.setFont(font)
        self.original_video_text.setObjectName("original_video_text")

        self.original_video1 = QtWidgets.QPushButton(self.side_bar1)
        self.original_video1.setGeometry(QtCore.QRect(20, 60, 100, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.original_video1.setFont(font)
        self.original_video1.setObjectName("original_video1")

        self.original_video2 = QtWidgets.QPushButton(self.side_bar1)
        self.original_video2.setGeometry(QtCore.QRect(160, 60, 100, 45))
        self.original_video2.setFont(font)
        self.original_video2.setObjectName("original_video2")

        self.original_video3 = QtWidgets.QPushButton(self.side_bar1)
        self.original_video3.setGeometry(QtCore.QRect(90, 115, 100, 45))
        self.original_video3.setFont(font)
        self.original_video3.setObjectName("original_video3")

        self.side_bar2 = QtWidgets.QFrame(self.centralwidget)
        self.side_bar2.setGeometry(QtCore.QRect(744, 250, 280, 180))
        self.side_bar2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_bar2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_bar2.setObjectName("side_bar2")

        self.person_track_text = QtWidgets.QLabel(self.side_bar2)
        self.person_track_text.setGeometry(QtCore.QRect(10, 10, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.person_track_text.setFont(font)
        self.person_track_text.setObjectName("person_track_text")

        self.person_track_video1 = QtWidgets.QPushButton(self.side_bar2)
        self.person_track_video1.setGeometry(QtCore.QRect(20, 60, 100, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.person_track_video1.setFont(font)
        self.person_track_video1.setObjectName("person_track_video1")

        self.person_track_video2 = QtWidgets.QPushButton(self.side_bar2)
        self.person_track_video2.setGeometry(QtCore.QRect(160, 60, 100, 45))
        self.person_track_video2.setFont(font)
        self.person_track_video2.setObjectName("person_track_video2")

        self.person_track_video3 = QtWidgets.QPushButton(self.side_bar2)
        self.person_track_video3.setGeometry(QtCore.QRect(90, 115, 100, 45))
        self.person_track_video3.setFont(font)
        self.person_track_video3.setObjectName("person_track_video3")

        self.side_bar3 = QtWidgets.QFrame(self.centralwidget)
        self.side_bar3.setGeometry(QtCore.QRect(744, 430, 280, 180))
        self.side_bar3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_bar3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_bar3.setObjectName("side_bar3")

        self.multiple_videos_track_text = QtWidgets.QLabel(self.side_bar3)
        self.multiple_videos_track_text.setGeometry(QtCore.QRect(10, 10, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.multiple_videos_track_text.setFont(font)
        self.multiple_videos_track_text.setObjectName("multiple_videos_track_text")

        self.multiple_videos_track_button = QtWidgets.QPushButton(self.side_bar3)
        self.multiple_videos_track_button.setGeometry(QtCore.QRect(65, 80, 150, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.multiple_videos_track_button.setFont(font)
        self.multiple_videos_track_button.setObjectName("multiple_videos_track_button")

        self.side_bar4 = QtWidgets.QFrame(self.centralwidget)
        self.side_bar4.setGeometry(QtCore.QRect(4, 566, 736, 44))
        self.side_bar4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_bar4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_bar4.setObjectName("side_bar4")

        # Button to open the video file dialog
        self.open_video_button = QtWidgets.QPushButton(self.side_bar4)
        self.open_video_button.setGeometry(QtCore.QRect(10, 2, 150, 40))
        self.open_video_button.setText("Choose Video")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.open_video_button.setFont(font)
        self.open_video_button.setObjectName("open_video_button")

        # Label to display the selected video name
        self.video_name_label = QtWidgets.QLabel(self.side_bar4)
        self.video_name_label.setGeometry(QtCore.QRect(170, 2, 245, 40))  # Adjusted for better spacing
        font.setUnderline(True)
        self.video_name_label.setFont(font)
        self.video_name_label.setObjectName("video_name_label")

        # Button to play the selected video
        self.play_video_button = QtWidgets.QPushButton(self.side_bar4)
        self.play_video_button.setGeometry(QtCore.QRect(421, 2, 155, 40))
        self.play_video_button.setText("Play Original Video")
        font.setUnderline(False)
        self.play_video_button.setFont(font)
        self.play_video_button.setObjectName("play_video_button")
        self.play_video_button.setEnabled(False)  # Initially disabled

        # Button to play the selected video
        self.play_video_button_person_tracking = QtWidgets.QPushButton(self.side_bar4)
        self.play_video_button_person_tracking.setGeometry(QtCore.QRect(576, 2, 150, 40))
        self.play_video_button_person_tracking.setText("Person Tracking")
        self.play_video_button_person_tracking.setFont(font)
        self.play_video_button_person_tracking.setObjectName("play_video_button")
        self.play_video_button_person_tracking.setEnabled(False)  # Initially disabled

        self.video_frame = QtWidgets.QFrame(self.centralwidget)
        self.video_frame.setGeometry(QtCore.QRect(4, 95, 736, 446))
        self.video_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_frame.setObjectName("video_frame")

        self.videoLabel = QtWidgets.QLabel(self.video_frame)
        self.videoLabel.setGeometry(0, 0, 736, 446)
        self.videoLabel.setObjectName("videoLabel")

        self.videoLabel1 = QtWidgets.QLabel(self.video_frame)
        self.videoLabel1.setGeometry(3, 2, 363, 220)
        self.videoLabel1.setObjectName("videoLabel1")

        self.videoLabel2 = QtWidgets.QLabel(self.video_frame)
        self.videoLabel2.setGeometry(366, 2, 363, 220)
        self.videoLabel2.setObjectName("videoLabel2")

        self.videoLabel3 = QtWidgets.QLabel(self.video_frame)
        self.videoLabel3.setGeometry(186, 224, 363, 220)
        self.videoLabel3.setObjectName("videoLabel3")

        self.mediaPlayer = None
        self.videoWidget = None

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)

        self.use_services()

    def use_services(self):
        """Connects UI elements to their corresponding functions."""

        self.original_video1.clicked.connect(lambda: self.play_video_after_stopping(os.getcwd() + "/videos/video1.mp4"))
        self.original_video2.clicked.connect(lambda: self.play_video_after_stopping(os.getcwd() + "/videos/video2.mp4"))
        self.original_video3.clicked.connect(lambda: self.play_video_after_stopping(os.getcwd() + "/videos/video3.mp4"))

        self.person_track_video1.clicked.connect(self.start_tracker_thread1)
        self.person_track_video2.clicked.connect(self.start_tracker_thread2)
        self.person_track_video3.clicked.connect(self.start_tracker_thread3)

        self.multiple_videos_track_button.clicked.connect(self.play_multiple_videos)
        self.open_video_button.clicked.connect(self.open_file_dialog)
        self.play_video_button.clicked.connect(self.play_selected_video)
        self.play_video_button_person_tracking.clicked.connect(self.person_tracking_selected_video)

    def open_file_dialog(self):
        """Open a file dialog to select a video file and display the file name."""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        video_file, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4)",
                                                    options=options)
        if video_file:
            self.selected_video_path = video_file
            self.play_video_button.setEnabled(True)
            self.play_video_button_person_tracking.setEnabled(True)
            # Extract the file name from the full path and display it
            file_name = os.path.basename(video_file)
            self.video_name_label.setText(f"Selected Video: {file_name}")
            print("Selected video:", self.selected_video_path)
        else:
            # Clear the label and set the buttons cannot be clicked if no file is selected
            self.video_name_label.setText("No video selected.")
            self.play_video_button.setEnabled(False)
            self.play_video_button_person_tracking.setEnabled(False)

    def play_selected_video(self):
        """Play the video from the selected path."""
        if hasattr(self, 'selected_video_path'):
            self.play_video_after_stopping(self.selected_video_path)
        else:
            print("No video file selected.")

    def person_tracking_selected_video(self):
        """Play the video from the selected path."""
        if hasattr(self, 'selected_video_path'):
            self.start_tracker_thread()
        else:
            print("No video file selected.")

    """
    Functions start_tracker_thread1, start_tracker_thread2, start_tracker_thread3 are similar and
    are used to stop current activities, prepare the UI, and start tracking on specified video sources.
    """
    def start_tracker_thread(self):
        self.stop_tracker_thread()
        self.destroy_media_components()
        self.hide_small_video_labels()
        self.videoLabel.show()
        self.tracker_thread1 = TrackerThread(self.selected_video_path)
        self.tracker_thread1.frame_ready.connect(lambda frame: self.display_frame(frame, self.videoLabel))
        self.tracker_thread1.start()

    def start_tracker_thread1(self):
        self.stop_tracker_thread()
        self.destroy_media_components()
        self.hide_small_video_labels()
        self.videoLabel.show()
        self.tracker_thread1 = TrackerThread("videos/video1.mp4")
        self.tracker_thread1.frame_ready.connect(lambda frame: self.display_frame(frame, self.videoLabel))
        self.tracker_thread1.start()

    def start_tracker_thread2(self):
        self.stop_tracker_thread()
        self.destroy_media_components()
        self.hide_small_video_labels()
        self.videoLabel.show()
        self.tracker_thread2 = TrackerThread("videos/video2.mp4")
        self.tracker_thread2.frame_ready.connect(lambda frame: self.display_frame(frame, self.videoLabel))
        self.tracker_thread2.start()

    def start_tracker_thread3(self):
        self.stop_tracker_thread()
        self.destroy_media_components()
        self.hide_small_video_labels()
        self.videoLabel.show()
        self.tracker_thread3 = TrackerThread("videos/video3.mp4")
        self.tracker_thread3.frame_ready.connect(lambda frame: self.display_frame(frame, self.videoLabel))
        self.tracker_thread3.start()

    def stop_tracker_thread(self):
        """Stops active tracking threads safely."""

        if hasattr(self, 'tracker_thread1'):
            print("Yes")
            self.tracker_thread1.stop()
        if hasattr(self, 'tracker_thread2'):
            self.tracker_thread2.stop()
        if hasattr(self, 'tracker_thread3'):
            self.tracker_thread3.stop()

    def destroy_media_components(self):
        """Cleans up media player components to release resources."""

        if self.mediaPlayer is not None:
            self.mediaPlayer.stop()
            self.mediaPlayer.disconnect()
            self.mediaPlayer.deleteLater()
            self.mediaPlayer = None

        if self.videoWidget is not None:
            self.videoWidget.hide()
            self.videoWidget.deleteLater()
            self.videoWidget = None

    def play_multiple_videos(self):
        """Track person in three videos simultaneously."""

        self.stop_tracker_thread()
        self.destroy_media_components()
        self.videoLabel.hide()
        self.show_small_video_labels()
        # Set an empty QPixmap to clear the video label
        self.videoLabel.setPixmap(QPixmap())

        # Initialize and start tracking threads for each video
        self.tracker_thread1 = TrackerThread("videos/video1.mp4")
        self.tracker_thread1.frame_ready.connect(lambda frame: self.display_frame(frame, self.videoLabel1))
        self.tracker_thread1.start()

        self.tracker_thread2 = TrackerThread("videos/video2.mp4")
        self.tracker_thread2.frame_ready.connect(lambda frame: self.display_frame(frame, self.videoLabel2))
        self.tracker_thread2.start()

        self.tracker_thread3 = TrackerThread("videos/video3.mp4")
        self.tracker_thread3.frame_ready.connect(lambda frame: self.display_frame(frame, self.videoLabel3))
        self.tracker_thread3.start()

    def play_video_after_stopping(self, video_path):
        """Stops any current video or tracking, then plays a new video."""

        self.stop_tracker_thread()
        self.hide_small_video_labels()
        # Set an empty QPixmap to clear the video label
        self.videoLabel.setPixmap(QPixmap())
        self.play_video(video_path)

    def hide_small_video_labels(self):
        self.videoLabel1.hide()
        self.videoLabel2.hide()
        self.videoLabel3.hide()

    def show_small_video_labels(self):
        self.videoLabel1.show()
        self.videoLabel2.show()
        self.videoLabel3.show()

    def display_frame(self, frame, target_label):
        """Updates the specified label with a new video frame."""

        # Convert OpenCV image to QImage
        height, width, channels = frame.shape
        bytesPerLine = 3 * width
        qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(qImg)

        # Scale QPixmap to fit the target label size
        scaled_pixmap = pixmap.scaled(target_label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

        # Update the specified QLabel's QPixmap
        target_label.setPixmap(scaled_pixmap)

    def play_video(self, video_path):
        """Method to play the original videos."""

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget(self.video_frame)
        self.videoWidget.setGeometry(0, 0, 736, 446)  # Adjust size to fill the frame.
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(video_path)))

        self.mediaPlayer.error.connect(self.handle_error)  # Handle media player error.
        self.mediaPlayer.play()
        self.videoWidget.show()

    def stop_all_activities(self):
        if hasattr(self, 'tracker_thread1'):
            self.tracker_thread1.stop()
        if hasattr(self, 'tracker_thread2'):
            self.tracker_thread2.stop()
        if hasattr(self, 'tracker_thread3'):
            self.tracker_thread3.stop()

    def handle_error(self):
        print("Current working directory:", os.getcwd())
        print("Error: ", self.mediaPlayer.errorString())

    def closeEvent(self, event):
        """Override closeEvent in super class to clear the resources used."""

        self.destroy_media_components()
        self.stop_tracker_thread()
        event.accept()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Person Tracking"))
        self.title.setText(_translate("MainWindow", "Person Tracking Application"))
        self.original_video_text.setText(_translate("MainWindow", "Original Videos"))
        self.person_track_text.setText(_translate("MainWindow", "Person Tracking"))
        self.multiple_videos_track_text.setText(_translate("MainWindow", "Person Tracking (Multiple)"))
        self.original_video1.setText(_translate("MainWindow", "Video1"))
        self.original_video2.setText(_translate("MainWindow", "Video2"))
        self.original_video3.setText(_translate("MainWindow", "Video3"))
        self.person_track_video1.setText(_translate("MainWindow", "Video1"))
        self.person_track_video2.setText(_translate("MainWindow", "Video2"))
        self.person_track_video3.setText(_translate("MainWindow", "Video3"))
        self.multiple_videos_track_button.setText(_translate("MainWindow", "Multiple Videos"))
