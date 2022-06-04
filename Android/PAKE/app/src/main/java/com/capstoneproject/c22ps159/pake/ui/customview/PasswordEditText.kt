package com.capstoneproject.c22ps159.pake.ui.customview

import android.content.Context
import android.graphics.Canvas
import android.graphics.drawable.Drawable
import android.text.Editable
import android.text.TextWatcher
import android.text.method.PasswordTransformationMethod
import android.util.AttributeSet
import android.view.MotionEvent
import android.view.View
import androidx.appcompat.widget.AppCompatEditText
import androidx.core.content.ContextCompat
import com.capstoneproject.c22ps159.pake.R

class PasswordEditText: AppCompatEditText, View.OnTouchListener {

    private val roundedBackground = ContextCompat.getDrawable(context, R.drawable.bg_edttext)
    private lateinit var hidePasswordIcon: Drawable
    private lateinit var showPasswordIcon: Drawable
    private var isHidden = true
    private val passwordTransformationMethod = PasswordTransformationMethod.getInstance()

    constructor(context: Context) : super(context) { init() }
    constructor(context: Context, attrs: AttributeSet) : super(context, attrs) { init() }
    constructor(context: Context, attrs: AttributeSet, defStyleAttr: Int) : super(
        context,
        attrs,
        defStyleAttr
    ) { init() }

    private fun init() {
        setOnTouchListener(this)
        addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(p0: CharSequence?, p1: Int, p2: Int, p3: Int) {}

            override fun onTextChanged(text: CharSequence?, p1: Int, p2: Int, p3: Int) {}

            override fun afterTextChanged(text: Editable?) {
                text?.let {
                    if (it.length < 6 && it.isNotBlank()) setError(context.applicationContext.getString(R.string.password_min), null)
                }
            }
        })
        hidePasswordIcon = ContextCompat.getDrawable(context, R.drawable.ic_hide_disabled) as Drawable
        showPasswordIcon =  ContextCompat.getDrawable(context, R.drawable.ic_hide) as Drawable
    }

    private fun setDrawables(
        left: Drawable? = null,
        top: Drawable? = null,
        right: Drawable? = null,
        bottom: Drawable? = null,
    ) {
        setCompoundDrawablesWithIntrinsicBounds(left, top, right, bottom)
    }

    private fun showPasswordVisible() {
        setDrawables(null, null, null, null)
        setDrawables(null, null, showPasswordIcon, null)
    }

    private fun showPasswordHidden() {
        setDrawables(null, null, null, null)
        setDrawables(null, null, hidePasswordIcon, null)
    }

    override fun onTouch(view: View?, event: MotionEvent): Boolean {
        if (compoundDrawables[2] != null) {
            val toggleButtonStart: Float
            val toggleButtonEnd: Float
            var isToggleButtonClicked = false

            if (layoutDirection == View.LAYOUT_DIRECTION_RTL) {
                toggleButtonEnd = (hidePasswordIcon.intrinsicWidth + paddingStart).toFloat()
                if (event.x < toggleButtonEnd) isToggleButtonClicked = true
            } else {
                toggleButtonStart = (width - paddingEnd - hidePasswordIcon.intrinsicWidth).toFloat()
                if (event.x > toggleButtonStart) isToggleButtonClicked = true
            }

            if (isToggleButtonClicked) {
                when (event.action) {
                    MotionEvent.ACTION_DOWN -> {
                        hidePasswordIcon = ContextCompat.getDrawable(context, R.drawable.ic_hide_disabled) as Drawable
                        showPasswordIcon =  ContextCompat.getDrawable(context, R.drawable.ic_hide) as Drawable
                        isHidden = !isHidden
                        return true
                    }
                }
            }
        }
        return false
    }

    override fun onDraw(canvas: Canvas?) {
        super.onDraw(canvas)
        background = roundedBackground
        transformationMethod = if (isHidden) {
            showPasswordVisible()
            passwordTransformationMethod
        } else {
            showPasswordHidden()
            null
        }
        textSize = 14F
        textAlignment = View.TEXT_ALIGNMENT_VIEW_START
    }
}