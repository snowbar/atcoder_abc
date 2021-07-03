//
//  main.swift
//  hoge
//
//  Created by snowbar on 2021/06/27.
//
//構造体
struct Point {
    let t: Int
    let x: Int
    let y: Int
}

func main() {
    //入力
    let n = Int(readLine()!)!
    let points: [Point] = (0...n)
        .compactMap { index in
            if index == 0 { return Point(t: 0, x: 0, y: 0) }
            let list = readLine()!.split(separator: " ")
                .compactMap { Int($0) }
            return Point(t: list[0], x: list[1], y: list[2])
        }
        .sorted {
            $0.t < $1.t
        }
    //出力
    print(isPossible(n: n, points: points) ? "Yes" : "No")
}

// ロジック
private func isPossible(n: Int, points: [Point]) -> Bool {
    (0...n).reduce(true) { ans, index in
        if n == 0 { return false }
        if index == n { return ans }
        
        let before = points[index]
        let after = points[index + 1]
        let t = after.t - before.t
        let d = abs(after.x - before.x) + abs(after.y - before.y)
        
        if d == 0 && t == 0 { return false }
        if d > t { return false }
        if d == t { return ans }
        if d < t {
            if (t - d) % 2 == 0 {
                return ans
            } else {
                return false
            }
        }
        return ans
    }
}
main()
