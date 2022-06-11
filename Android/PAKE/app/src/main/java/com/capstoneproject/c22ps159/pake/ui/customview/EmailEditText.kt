package com.capstoneproject.c22ps159.pake.ui.customview

import android.content.Context
import android.graphics.Canvas
import android.graphics.drawable.Drawable
import android.text.Editable
import android.text.TextWatcher
import android.util.AttributeSet
import android.util.Patterns
import android.view.MotionEvent
import android.view.View
import androidx.core.content.ContextCompat
import com.capstoneproject.c22ps159.pake.R
import com.google.android.material.textfield.TextInputEditText

class EmailEditText: TextInputEditText{
    private val roundedBackground =
        ContextCompat.getDrawable(context, R.drawable.bg_edttext)
    private lateinit var clearButtonImage: Drawable

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
        clearButtonImage = ContextCompat.getDrawable(context, R.drawable.ic_close) as Drawable

        addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(p0: CharSequence?, p1: Int, p2: Int, p3: Int) {
            }

            override fun onTextChanged(text: CharSequence?, p1: Int, p2: Int, p3: Int) {

            }

            override fun afterTextChanged(text: Editable?) {
                text?.let {
                    if (text.isNotEmpty() && !Patterns.EMAIL_ADDRESS.matcher(it).matches())
                        error = context.applicationContext.getString(R.string.email_not_valid)
                }
            }
        })
    }

    // Menampilkan clear button


    //Mengkonfigurasi button
    private fun setButtonDrawables(startOfTheText: Drawable? = null, topOfTheText:Drawable? = null, endOfTheText:Drawable? = null, bottomOfTheText: Drawable? = null){
        setCompoundDrawablesWithIntrinsicBounds(startOfTheText, topOfTheText, endOfTheText, bottomOfTheText)
    }

    override fun onDraw(canvas: Canvas?) {
        super.onDraw(canvas)
        background = roundedBackground
        textSize = 14F
        textAlignment = View.TEXT_ALIGNMENT_VIEW_START
    }

}