package com.capstoneproject.c22ps159.pake.ui.customview

import android.content.Context
import android.graphics.Canvas
import android.text.Editable
import android.text.TextWatcher
import android.util.AttributeSet
import android.view.View
import androidx.appcompat.widget.AppCompatEditText
import androidx.core.content.ContextCompat
import com.capstoneproject.c22ps159.pake.R

class FormEditText: AppCompatEditText{
    private val roundedBackground =
        ContextCompat.getDrawable(context, R.drawable.bg_edttext)

    constructor(context: Context) : super(context) {
        init()
    }

    constructor(context: Context, attrs: AttributeSet) : super(context, attrs) {
        init()
    }

    constructor(context: Context, attrs: AttributeSet, defStyleAttr: Int) : super(
        context,
        attrs,
        defStyleAttr
    ) {
        init()
    }

    private fun init() {

        addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(p0: CharSequence?, p1: Int, p2: Int, p3: Int) {
            }

            override fun onTextChanged(text: CharSequence?, p1: Int, p2: Int, p3: Int) {
            }

            override fun afterTextChanged(text: Editable?) {
                text?.let {
                    if (text.isEmpty())
                        error = context.applicationContext.getString(R.string.fill_the_form)
                }
            }
        })
    }

    override fun onDraw(canvas: Canvas?) {
        super.onDraw(canvas)
        background = roundedBackground
        textSize = 14F
        textAlignment = View.TEXT_ALIGNMENT_VIEW_START
    }
}