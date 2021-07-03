//
//  main.swift
//  abc
//
//  Created by snowbar on 2021/06/27.
//

func main() {
    let list = readLine()!.split(separator: " ").compactMap { Int($0) }
    print(hoge(a: list[0], b: list[1], c: list[2], d: list[3]))
}

func hoge(a: Int, b: Int, c: Int, d: Int) -> Int {
    if (a + b) <= c * d {
        return 1
    } else if b >= c * d {
        return -1
    }
    
    var count = 0
    var blueBallCount = a
    var redBallCount = 0
    while blueBallCount > redBallCount * d {
        blueBallCount += b
        redBallCount += c
        count += 1
    }
    return count
}

main()
