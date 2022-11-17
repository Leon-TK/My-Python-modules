These modules works with my TODO convention

regex with my notation - `COMMENT_CHAR`[^S\r\n]*TODO:[^S\r\n]*\s
Where COMMENT_CHAR is language specific comment char

In other words - CommentChar + any chars except \r and \n + TODO: + any chars except \r and \n + newline

Any TODO line can contain nested TODOs. You must use `TODO:`, else this will not be counted