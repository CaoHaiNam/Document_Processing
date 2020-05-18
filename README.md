# Document_Processing
Tiền xử lý trong bài toán toán phân loại văn bản theo chủ đề áp dụng kỹ thuật naive bayes, có xử lý từ viết tắt
Phân loại Naive Bayes là một kỹ thuật nổi tiếng và được áp dụng rất nhiều trong các bài toán phân loại văn bản. Trong đó, công đoạn tách từ
(feature extraction) có vai trò rất quan trọng. Đối với văn bản tiếng Việt, việc tách từ(token) không chỉ dựa vào dấu cách(space) mà phức 
tạp hơn(lấy ví dụ đơn giản: nước, ngoài và nước_ngoài hoàn toàn khác nhau). Vì vậy, có một số công cụ public để thực hiện công việc này(pyvi,
Vi_spacy đều của tác giả Trần Việt Trung, phoBert của VinAI). Trong project của tôi, tôi sử dụng Pyvi.

 Điềm khác biệt trong trong project này, đó là quan tâm đến việc xử lý từ viết tắt(ví dụ: ubnd: ủ ban nhân dân). Hiện tại, công việc này 
 đang được thực hiện bằng tay, nhưng có sử dụng một số tri thức để việc làm này diễn ra nhanh hơn.
 
 Nhận thấy những từ viết tắt đều là nhưng từ đơn, và không có các dấu thanh ở trong đó(dấu hỏi, ngã,...), vì vậy, để tìm các từ viết tắt, 
 ta chỉ cần kiểm tra các từ có tính chất trên(file Check_dau_thanh.py). Từ đó, việc phát hiện ra nhưng từ viết tắt sẽ nhanh hơn.
 
 Vấn đề tồn tại ở đây là: đôi khi cùng là 1 từ viết tắt, nhưng có thể có 2 ý nghĩa khác nhau(ttlt: có thể hiển là trung tâm luyện thi hoặc
 là thông tư liên tịch).
 
# Hướng dẫn cài đặt:
Bộ dữ liệu đầy đủ: https://github.com/duyvuleo/VNTC/tree/master/Data (trong project trên tôi chỉ trích ra 1 phần nhỏ cho việc kiểm tra tính 
hiệu quả của nó)
Cài đặt thư viện pyvi: vào cmd, gõ lệnh: pip install pyvi để hoàn tất cài đặt (giả sử máy tính đã cài đặt pip)
Sau khi download Project về, giải nén file data và cho nó vào cùng thư mục của thư mục vừa tải về, ta được thư mục data.
Chạy file word_exist_arc.py, ta đc file json chứa các từ của các topic, chứa từ viết tắt, nằm trong thư mục data/word_exist_arc.
Chạy file word_without_arc.py, ta đc file json chứa các từ của các topic, không chứa từ viết tắt, nằm trong thư mục data/word_without_arc.

