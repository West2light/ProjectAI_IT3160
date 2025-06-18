# Project AI IT3160 - Thief and Police

## Giới thiệu
Dự án game "Thief and Police" sử dụng các thuật toán AI để mô phỏng cuộc truy đuổi giữa tội phạm và cảnh sát. Game được phát triển bằng Python và Pygame với 4 level khác nhau, mỗi level sử dụng một thuật toán AI khác nhau.

## Cấu trúc thư mục

```
ProjectAI_IT3160/
├── README.md                    # Tài liệu hướng dẫn
├── Input/                       # Các file bản đồ đầu vào
│   ├── Level1/                  # Bản đồ Level 1
│   │   ├── map1.txt
│   │   ├── map2.txt
│   │   ├── map3.txt
│   │   ├── map4.txt
│   │   └── map5.txt
│   ├── Level2/                  # Bản đồ Level 2
│   │   ├── map1.txt
│   │   ├── map2.txt
│   │   ├── map3.txt
│   │   ├── map4.txt
│   │   └── map5.txt
│   ├── Level3/                  # Bản đồ Level 3
│   │   ├── map1.txt
│   │   ├── map2.txt
│   │   ├── map3.txt
│   │   ├── map4.txt
│   │   └── map5.txt
│   └── Level4/                  # Bản đồ Level 4
│       ├── map1.txt
│       ├── map2.txt
│       ├── map3.txt
│       ├── map4.txt
│       └── map5.txt
├── Source/                      # Mã nguồn chính
│   ├── main.py                  # File chính để chạy game
│   ├── constants.py             # Các hằng số và cấu hình
│   ├── Algorithms/              # Các thuật toán AI
│   │   ├── BFS.py              # Thuật toán Breadth-First Search
│   │   ├── DFS.py              # Thuật toán Depth-First Search
│   │   ├── LocalSearch.py      # Thuật toán Local Search
│   │   ├── Minimax.py          # Thuật toán Minimax
│   │   ├── Police_Move.py      # Logic di chuyển cảnh sát
│   │   └── SearchAlgorithms.py # Interface các thuật toán tìm kiếm
│   ├── Extension/               # Các tính năng mở rộng
│   │   └── extension.py
│   ├── images/                  # Tài nguyên hình ảnh
│   │   ├── gameover.png
│   │   ├── home.png
│   │   ├── police1.png
│   │   ├── police2.png
│   │   ├── police3.png
│   │   ├── police4.png
│   │   ├── thief.png
│   │   ├── win.png
│   │   └── win1.png
│   └── Object/                  # Các đối tượng trong game
│       ├── Food.py             # Đối tượng thức ăn
│       ├── Menu.py             # Menu game
│       ├── Player.py           # Đối tượng người chơi (tội phạm)
│       └── Wall.py             # Đối tượng tường
```

## Cài đặt và Chạy chương trình

### Bước 1: Clone Repository
```bash
git clone https://github.com/West2light/ProjectAI_IT3160.git
cd Source
```

### Bước 2: Cài đặt Python và Dependencies
1. Cài đặt Python từ trang chủ [python.org](https://python.org)
2. Cài đặt Pygame:
   ```bash
   pip install pygame
   ```
   Hoặc cài đặt từ file requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

### Bước 3: Chạy chương trình
Mở console tại thư mục `Source` và chạy lệnh:
```bash
py main.py
```
hoặc
```bash
python main.py
```

## Mô tả Game

Game "Thief and Police" là một trò chơi mô phỏng cuộc truy đuổi giữa tội phạm và cảnh sát trên một bản đồ 2D. Mục tiêu của tội phạm là thu thập thức ăn trong khi tránh bị cảnh sát bắt.

### Các Level Game

#### Level 1: DFS - Depth First Search
- **Mô tả**: Tội phạm biết vị trí thức ăn, không có cảnh sát
- **Thuật toán**: Depth First Search
- **Đặc điểm**: Chỉ có một thức ăn trên bản đồ
- **Hoàn thành**: 100%

#### Level 2: BFS - Breadth First Search  
- **Mô tả**: Có cảnh sát nhưng không di chuyển, va chạm = thua cuộc
- **Thuật toán**: Breadth-First Search
- **Đặc điểm**: Tìm đường đi ngắn nhất đến thức ăn
- **Hoàn thành**: 100%

#### Level 3: Local Search
- **Mô tả**: Tầm nhìn tội phạm giới hạn 3 đơn vị, cảnh sát di chuyển từng bước
- **Thuật toán**: Heuristic Local Search
- **Đặc điểm**: Nhiều thức ăn, cảnh sát di chuyển quanh vị trí ban đầu
- **Hoàn thành**: 100%

#### Level 4: Minimax + A*
- **Mô tả**: Bản đồ kín, cảnh sát truy đuổi tích cực
- **Thuật toán**: Minimax cho tội phạm, A* cho cảnh sát
- **Đặc điểm**: Cảnh sát có thể đi xuyên qua nhau, rất nhiều thức ăn
- **Hoàn thành**: 100%

## So sánh Thuật toán

| Thuật toán | Ưu điểm | Nhược điểm | Ứng dụng |
|------------|---------|------------|-----------|
| **DFS** | Đơn giản, ít bộ nhớ | Đường đi dài | Duyệt toàn bộ map |
| **BFS** | Tìm đường gần nhất | Tốn bộ nhớ | Tránh cảnh sát, ăn điểm gần |
| **Local Search** | Nhanh, heuristic linh hoạt | Dễ mắc kẹt local maxima | Di chuyển real-time |
| **Minimax** | Tối ưu với đối thủ | Độ phức tạp cao | Cảnh sát AI hoặc tội phạm phức tạp |

## Đánh giá Hoàn thành

| STT | Yêu cầu | Thực hiện | Hoàn thành |
|-----|---------|-----------|-------------|
| 1 | Level 1: DFS | Depth First Search | 100% |
| 2 | Level 2: BFS | Breadth-First Search | 100% |
| 3 | Level 3: Local Search | Heuristic Local Search | 100% |
| 4 | Level 4: Minimax + A* | Minimax + A* | 100% |
| 5 | Biểu diễn đồ họa | Pygame | 100% |
| 6 | Tạo 5 bản đồ khác nhau | Có 5 map cho mỗi level | 100% |
| 7 | Báo cáo thuật toán | Hoàn thành | 100% |

## Công nghệ sử dụng

- **Python**: Ngôn ngữ lập trình chính
- **Pygame**: Thư viện đồ họa và game
- **Các thuật toán AI**: DFS, BFS, Local Search, Minimax, A*

## Tác giả

Dự án được phát triển trong khuôn khổ môn học AI IT3160.